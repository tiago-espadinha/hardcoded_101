#include "server.h"
#include "thread_pool.h"
#include "rooms.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/socket.h>
#include <signal.h>

static ThreadPool *tp = NULL;
volatile sig_atomic_t shutdown_flag = 0;

void handle_client(void *arg) {
    int client_fd = *(int*)arg;
    free(arg);

    rooms_set_nick(client_fd, "");
    rooms_join(client_fd, "general");

    const char *welcome = "[SERVER] Welcome to chatd! You are in 'general'.\n";
    send(client_fd, welcome, strlen(welcome), 0);

    char buf[1024];
    while (!shutdown_flag) {
        ssize_t n = recv(client_fd, buf, sizeof(buf) - 1, 0);
        if (n <= 0) break;
        buf[n] = '\0';
        
        // Basic line trimming
        char *line = strtok(buf, "\r\n");
        while (line) {
            if (line[0] == '/') {
                if (strncmp(line, "/nick ", 6) == 0) {
                    rooms_set_nick(client_fd, line + 6);
                } else if (strncmp(line, "/join ", 6) == 0) {
                    rooms_join(client_fd, line + 6);
                } else if (strcmp(line, "/leave") == 0) {
                    rooms_leave(client_fd);
                    rooms_join(client_fd, "general");
                } else if (strcmp(line, "/list") == 0) {
                    rooms_list(client_fd);
                } else if (strcmp(line, "/who") == 0) {
                    rooms_who(client_fd);
                } else if (strncmp(line, "/msg ", 5) == 0) {
                    char *target = line + 5;
                    char *msg = strchr(target, ' ');
                    if (msg) {
                        *msg = '\0';
                        rooms_private_msg(client_fd, target, msg + 1);
                    }
                }
            } else {
                // Broadcast to current room
                char current_room[32] = {0};
                rooms_get_current_room(client_fd, current_room);
                if (current_room[0]) {
                    rooms_broadcast(client_fd, line, current_room);
                }
            }
            line = strtok(NULL, "\r\n");
        }
    }

    rooms_remove_client(client_fd);
    close(client_fd);
}

void sig_handler(int sig) {
    (void)sig;
    shutdown_flag = 1;
}

void start_server(int port) {
    signal(SIGINT, sig_handler);
    signal(SIGTERM, sig_handler);

    int server_fd = socket(AF_INET, SOCK_STREAM, 0);
    int opt = 1;
    setsockopt(server_fd, SOL_SOCKET, SO_REUSEADDR, &opt, sizeof(opt));

    struct sockaddr_in addr;
    addr.sin_family = AF_INET;
    addr.sin_addr.s_addr = INADDR_ANY;
    addr.sin_port = htons(port);

    bind(server_fd, (struct sockaddr*)&addr, sizeof(addr));
    listen(server_fd, 10);

    tp = tp_create(THREAD_POOL_SIZE);
    rooms_init();

    printf("Server listening on port %d\n", port);

    while (!shutdown_flag) {
        struct sockaddr_in client_addr;
        socklen_t addr_len = sizeof(client_addr);
        int client_fd = accept(server_fd, (struct sockaddr*)&client_addr, &addr_len);
        if (client_fd < 0) {
            if (shutdown_flag) break;
            continue;
        }

        int *arg = malloc(sizeof(int));
        *arg = client_fd;
        tp_submit(tp, handle_client, arg);
    }

    tp_destroy(tp);
    close(server_fd);
}

int main(int argc, char *argv[]) {
    int port = DEFAULT_PORT;
    if (argc > 1) port = atoi(argv[1]);
    start_server(port);
    return 0;
}
