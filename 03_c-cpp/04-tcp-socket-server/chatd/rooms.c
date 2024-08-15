#include "rooms.h"
#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <pthread.h>
#include <sys/socket.h>

static Room rooms[MAX_ROOMS];
static Client clients[MAX_CLIENTS];
static pthread_mutex_t clients_lock = PTHREAD_MUTEX_INITIALIZER;

void rooms_init() {
    for (int i = 0; i < MAX_ROOMS; i++) {
        memset(&rooms[i], 0, sizeof(Room));
        pthread_mutex_init(&rooms[i].lock, NULL);
    }
    for (int i = 0; i < MAX_CLIENTS; i++) {
        clients[i].fd = -1;
        memset(clients[i].nick, 0, sizeof(clients[i].nick));
        memset(clients[i].current_room, 0, sizeof(clients[i].current_room));
    }
}

void rooms_set_nick(int client_fd, const char *nick) {
    pthread_mutex_lock(&clients_lock);
    for (int i = 0; i < MAX_CLIENTS; i++) {
        if (clients[i].fd == client_fd) {
            strncpy(clients[i].nick, nick, 20);
            clients[i].nick[20] = '\0';
            break;
        } else if (clients[i].fd == -1) {
            clients[i].fd = client_fd;
            strncpy(clients[i].nick, nick, 20);
            clients[i].nick[20] = '\0';
            break;
        }
    }
    pthread_mutex_unlock(&clients_lock);
}

int rooms_join(int client_fd, const char *room_name) {
    rooms_leave(client_fd);

    for (int i = 0; i < MAX_ROOMS; i++) {
        pthread_mutex_lock(&rooms[i].lock);
        if (rooms[i].count > 0 && strcmp(rooms[i].name, room_name) == 0) {
            if (rooms[i].count < MAX_USERS_PER_ROOM) {
                rooms[i].client_fds[rooms[i].count++] = client_fd;
                pthread_mutex_unlock(&rooms[i].lock);
                pthread_mutex_lock(&clients_lock);
                for (int j = 0; j < MAX_CLIENTS; j++) {
                    if (clients[j].fd == client_fd) {
                        strncpy(clients[j].current_room, room_name, 31);
                        break;
                    }
                }
                pthread_mutex_unlock(&clients_lock);
                return 0;
            }
            pthread_mutex_unlock(&rooms[i].lock);
            return -1;
        }
        pthread_mutex_unlock(&rooms[i].lock);
    }

    for (int i = 0; i < MAX_ROOMS; i++) {
        pthread_mutex_lock(&rooms[i].lock);
        if (rooms[i].count == 0) {
            strncpy(rooms[i].name, room_name, 31);
            rooms[i].client_fds[rooms[i].count++] = client_fd;
            pthread_mutex_unlock(&rooms[i].lock);
            pthread_mutex_lock(&clients_lock);
            for (int j = 0; j < MAX_CLIENTS; j++) {
                if (clients[j].fd == client_fd) {
                    strncpy(clients[j].current_room, room_name, 31);
                    break;
                }
            }
            pthread_mutex_unlock(&clients_lock);
            return 0;
        }
        pthread_mutex_unlock(&rooms[i].lock);
    }
    return -1;
}

void rooms_leave(int client_fd) {
    pthread_mutex_lock(&clients_lock);
    char room_name[32] = {0};
    for (int i = 0; i < MAX_CLIENTS; i++) {
        if (clients[i].fd == client_fd) {
            strcpy(room_name, clients[i].current_room);
            memset(clients[i].current_room, 0, 32);
            break;
        }
    }
    pthread_mutex_unlock(&clients_lock);

    if (room_name[0] == '\0') return;

    for (int i = 0; i < MAX_ROOMS; i++) {
        pthread_mutex_lock(&rooms[i].lock);
        if (strcmp(rooms[i].name, room_name) == 0) {
            for (int j = 0; j < rooms[i].count; j++) {
                if (rooms[i].client_fds[j] == client_fd) {
                    rooms[i].client_fds[j] = rooms[i].client_fds[--rooms[i].count];
                    break;
                }
            }
            if (rooms[i].count == 0) memset(rooms[i].name, 0, 32);
            pthread_mutex_unlock(&rooms[i].lock);
            return;
        }
        pthread_mutex_unlock(&rooms[i].lock);
    }
}

void rooms_list(int client_fd) {
    char buf[1024] = "[SERVER] Rooms:\n";
    for (int i = 0; i < MAX_ROOMS; i++) {
        pthread_mutex_lock(&rooms[i].lock);
        if (rooms[i].count > 0) {
            char line[64];
            snprintf(line, 64, "  - %s (%d users)\n", rooms[i].name, rooms[i].count);
            strcat(buf, line);
        }
        pthread_mutex_unlock(&rooms[i].lock);
    }
    send(client_fd, buf, strlen(buf), 0);
}

void rooms_who(int client_fd) {
    pthread_mutex_lock(&clients_lock);
    char room_name[32] = {0};
    for (int i = 0; i < MAX_CLIENTS; i++) {
        if (clients[i].fd == client_fd) {
            strcpy(room_name, clients[i].current_room);
            break;
        }
    }
    pthread_mutex_unlock(&clients_lock);

    if (room_name[0] == '\0') return;

    char buf[1024];
    snprintf(buf, 1024, "[SERVER] Users in %s:\n", room_name);
    for (int i = 0; i < MAX_ROOMS; i++) {
        pthread_mutex_lock(&rooms[i].lock);
        if (strcmp(rooms[i].name, room_name) == 0) {
            for (int j = 0; j < rooms[i].count; j++) {
                int f = rooms[i].client_fds[j];
                pthread_mutex_lock(&clients_lock);
                for (int k = 0; k < MAX_CLIENTS; k++) {
                    if (clients[k].fd == f) {
                        strcat(buf, "  - ");
                        strcat(buf, clients[k].nick[0] ? clients[k].nick : "anonymous");
                        strcat(buf, "\n");
                        break;
                    }
                }
                pthread_mutex_unlock(&clients_lock);
            }
            pthread_mutex_unlock(&rooms[i].lock);
            break;
        }
        pthread_mutex_unlock(&rooms[i].lock);
    }
    send(client_fd, buf, strlen(buf), 0);
}

void rooms_broadcast(int sender_fd, const char *message, const char *room_name) {
    char nick[21] = "anonymous";
    pthread_mutex_lock(&clients_lock);
    for (int i = 0; i < MAX_CLIENTS; i++) {
        if (clients[i].fd == sender_fd) {
            if (clients[i].nick[0]) strcpy(nick, clients[i].nick);
            break;
        }
    }
    pthread_mutex_unlock(&clients_lock);

    char buf[1024];
    snprintf(buf, 1024, "[%s] %s: %s\n", room_name, nick, message);

    for (int i = 0; i < MAX_ROOMS; i++) {
        pthread_mutex_lock(&rooms[i].lock);
        if (strcmp(rooms[i].name, room_name) == 0) {
            for (int j = 0; j < rooms[i].count; j++) {
                if (rooms[i].client_fds[j] != sender_fd) {
                    send(rooms[i].client_fds[j], buf, strlen(buf), 0);
                }
            }
            pthread_mutex_unlock(&rooms[i].lock);
            break;
        }
        pthread_mutex_unlock(&rooms[i].lock);
    }
}

void rooms_private_msg(int sender_fd, const char *target_nick, const char *message) {
    char from_nick[21] = "anonymous";
    pthread_mutex_lock(&clients_lock);
    int target_fd = -1;
    for (int i = 0; i < MAX_CLIENTS; i++) {
        if (clients[i].fd == sender_fd) {
            if (clients[i].nick[0]) strcpy(from_nick, clients[i].nick);
        }
        if (strcmp(clients[i].nick, target_nick) == 0) {
            target_fd = clients[i].fd;
        }
    }
    pthread_mutex_unlock(&clients_lock);

    if (target_fd != -1) {
        char buf[1024];
        snprintf(buf, 1024, "[DM] %s: %s\n", from_nick, message);
        send(target_fd, buf, strlen(buf), 0);
    } else {
        const char *err = "[SERVER] User not found.\n";
        send(sender_fd, err, strlen(err), 0);
    }
}

void rooms_remove_client(int client_fd) {
    rooms_leave(client_fd);
    pthread_mutex_lock(&clients_lock);
    for (int i = 0; i < MAX_CLIENTS; i++) {
        if (clients[i].fd == client_fd) {
            clients[i].fd = -1;
            memset(clients[i].nick, 0, 21);
            memset(clients[i].current_room, 0, 32);
            break;
        }
    }
    pthread_mutex_unlock(&clients_lock);
}
