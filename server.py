import socket, time, select

DEF_PORT: int = 8080


def run_server() -> None:
    sock = socket.socket()
    sock.setblocking(False)
    sock.bind(('', DEF_PORT))

    print(f'Socket bound on port: {DEF_PORT}')
    sock.listen()

    all_sockets: list = [ sock ]
    outputs: list = []

    # Listen for connections until max met
    while True:
        current, writable, exceptional = select.select(all_sockets, outputs, all_sockets)

        try:
            for con in current:
                if con is sock:
                    connection, addr = sock.accept()

                    # Add to client lists
                    if connection not in all_sockets:
                        all_sockets.append(connection)
                        connection.setblocking(False)
                    else:
                        print(f'New connection from: {addr}')
                else:
                    data = con.recv(1024)

                    if data:
                        print(f'Message from client[{con}]: {data}')
        except socket.error as err:
            # Socket isn't ready for comms
            time.sleep(0.25)


# Entry
if __name__ == '__main__':
    run_server()