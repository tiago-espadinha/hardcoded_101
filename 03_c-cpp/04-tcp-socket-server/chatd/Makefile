CC = gcc
CFLAGS = -std=c17 -Wall -Wextra -Werror -pthread
LDFLAGS = -pthread

all: chatd client

chatd: server.o thread_pool.o rooms.o
	$(CC) $(LDFLAGS) -o chatd server.o thread_pool.o rooms.o

client: client.o
	$(CC) $(LDFLAGS) -o client client.o

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -f *.o chatd client
