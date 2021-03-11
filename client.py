import socket
import sys

DEF_ADDR: tuple = ('127.0.0.1', 8080)


def connect_server() -> None:
    sock = socket.socket()

    # Try to connect to the address on port 8080 (localhost)
    try:
        print(f'Attempting to connect on - {DEF_ADDR[0]}:{DEF_ADDR[1]} ... ', end='')
        sock.connect((DEF_ADDR[0], DEF_ADDR[1]))
    except ConnectionRefusedError:
        print('Connection was refused! Server may be down.')
        sys.exit()

    print('Success!')
    sock.setblocking(False)

    while True:
        msg_server: bytes = sock.recv(1024)

        # Disconnected from server
        if len(msg_server) == 0:
            print(f'Connection from server broken.')
            break
        else:
            print(f'Recv: {msg_server}')

        msg: str = input('Enter message: ')

        # Close connection
        if (len(msg) == 0):
            msg = f'hello from {DEF_ADDR[0]}:{DEF_ADDR[1]}'
        msg: bytes = msg.encode('UTF-8')

        sock.send(msg)
    sock.close()


# Entry
if __name__ == '__main__':
    connect_server()