#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <pthread.h>
#include <signal.h>

void *read_server(void *arg) {
    int fd = *(int*)arg;
    char buf[1024];
    while (1) {
        ssize_t n = recv(fd, buf, sizeof(buf) - 1, 0);
        if (n <= 0) break;
        buf[n] = '\0';
        printf("%s", buf);
        fflush(stdout);
    }
    printf("Server disconnected.\n");
    exit(0);
    return NULL;
}

int main(int argc, char *argv[]) {
    if (argc < 3) {
        fprintf(stderr, "Usage: %s <host> <port>\n", argv[0]);
        return 1;
    }

    const char *host = argv[1];
    int port = atoi(argv[2]);

    int fd = socket(AF_INET, SOCK_STREAM, 0);
    struct sockaddr_in addr;
    addr.sin_family = AF_INET;
    addr.sin_port = htons(port);
    inet_pton(AF_INET, host, &addr.sin_addr);

    if (connect(fd, (struct sockaddr*)&addr, sizeof(addr)) < 0) {
        perror("connect");
        return 1;
    }

    pthread_t thread;
    pthread_create(&thread, NULL, read_server, &fd);

    char buf[1024];
    while (fgets(buf, sizeof(buf), stdin)) {
        send(fd, buf, strlen(buf), 0);
    }

    close(fd);
    return 0;
}
