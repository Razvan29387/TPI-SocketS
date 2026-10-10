    #!/usr/bin/env python
# Python Network Programming Cookbook, Second Edition -- Chapter 1
# This program is optimized for Python 3 and may also run on older versions.

import argparse
import socket

HOST = "0.0.0.0"
DATA_PAYLOAD = 2048
BACKLOG = 5


def echo_server(port, host=HOST):
    """A simple echo server."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_address = (host, port)
    print(f"Starting up echo server on {host} port {port}")
    sock.bind(server_address)
    sock.listen(BACKLOG)

    try:
        while True:
            print("Waiting to receive message from client")
            client, address = sock.accept()
            with client:
                data = client.recv(DATA_PAYLOAD)
                if data:
                    print(f"Data: {data!r}")
                    client.sendall(data)
                    print(f"sent {len(data)} bytes back to {address}")
    finally:
        sock.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Socket Server Example")
    parser.add_argument(
        "--port",
        action="store",
        dest="port",
        type=int,
        default=5000,
        help="port to listen on (default: 5000)",
    )
    args = parser.parse_args()
    echo_server(args.port)
