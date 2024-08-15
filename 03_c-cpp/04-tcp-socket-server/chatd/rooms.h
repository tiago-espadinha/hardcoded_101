#ifndef ROOMS_H
#define ROOMS_H

#include <pthread.h>

#define MAX_ROOMS 10
#define MAX_USERS_PER_ROOM 20
#define MAX_CLIENTS 100

typedef struct {
    int fd;
    char nick[21];
    char current_room[32];
} Client;

typedef struct {
    char name[32];
    int client_fds[MAX_USERS_PER_ROOM];
    int count;
    pthread_mutex_t lock;
} Room;

void rooms_init();
int rooms_join(int client_fd, const char *room_name);
void rooms_leave(int client_fd);
void rooms_list(int client_fd);
void rooms_who(int client_fd);
void rooms_broadcast(int sender_fd, const char *message, const char *room_name);
void rooms_private_msg(int sender_fd, const char *target_nick, const char *message);
void rooms_set_nick(int client_fd, const char *nick);
void rooms_remove_client(int client_fd);

#endif
