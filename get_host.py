import socket
import sys

DEF_PORT: int = 80


def connect_to_host(hostname: str) -> None:
    # Create a socket
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print('Successfully created a socket!')
    except socket.error as err:
        print(f'Socket failed to create with error: {err}')

    # Get IP from hostname
    try:
        host_ip: str = socket.gethostbyname(hostname)
    except socket.gaierror:
        print('Error resolving the host!')
        sys.exit()

    sock.connect((host_ip, DEF_PORT))
    print(f'Successfully connected to: {hostname} at {host_ip}')


# Entry
if __name__ == '__main__':
    host: str = input('Enter a hostname [Default Google.com]: ')

    if len(host) == 0:
        host = 'google.com'
    connect_to_host(host)