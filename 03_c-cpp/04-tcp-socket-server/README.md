# Module Name: chatd - TCP Socket Server in C

A multi-client TCP chat server implementation using POSIX sockets and pthreads, featuring a thread pool and room management.

## Features
- **Multi-threaded Server**: Uses a custom thread pool to handle up to 100 simultaneous connections efficiently.
- **Room Management**: Supports multiple chat rooms with a default "general" room and private messaging.
- **Graceful Shutdown**: Handles SIGINT and SIGTERM to ensure all resources are freed and connections closed cleanly.
- **Interactive Client**: A multi-threaded client for real-time communication.

## Learning Objectives
- Implement complex logic without relying on third-party magic.
- Understand the underlying mechanics of TCP connections, sockets, and multi-threaded synchronization.
- Analyze performance characteristics using real-world load testing.

## Project Structure
- `server.c`, `server.h`: Core server logic and socket handling.
- `thread_pool.c`, `thread_pool.h`: Custom thread pool implementation.
- `rooms.c`, `rooms.h`: Chat room and user management logic.
- `client.c`: Multi-threaded client implementation.
- `tests/`: Load tests and protocol verification scripts.

## Requirements
- GCC (C17 support)
- POSIX-compliant system (Linux recommended)
- Python 3 for running tests

## How to Run
Compile the server and client using the provided Makefile:
```bash
make
./chatd
./client localhost 8080
```

## Testing
Run the protocol tests:
```bash
python3 tests/test_protocol.py
```
Or the load tests:
```bash
python3 tests/load_test.py
```

## How to Use the Chat

### Start the Server
```bash
./chatd
# or specify a custom port: ./chatd 8080
```

### Connect as a Client
```bash
./client localhost 8080
```

### Commands
All commands are prefixed with `/`:

| Command | Description |
|---------|-------------|
| `/nick <name>` | Set your nickname |
| `/join <room>` | Join or create a room |
| `/leave` | Leave current room (returns to `general`) |
| `/list` | List all available rooms |
| `/who` | Show users in current room |
| `/msg <user> <message>` | Send a private message to a user |

**Regular messages** (without `/`) are broadcast to everyone in your current room.

### Example Session
**Terminal 1 - Start server:**
```bash
./chatd
```

**Terminal 2 - Connect as Alice:**
```bash
./client localhost 8080
> /nick Alice
> /join general
> Hello everyone!
```

**Terminal 3 - Connect as Bob:**
```bash
./client localhost 8080
> /nick Bob
> /join general
> Hi Alice!
> /msg Alice Hey privately
```
