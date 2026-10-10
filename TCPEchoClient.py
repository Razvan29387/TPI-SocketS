#!/usr/bin/env python
"""Connect to the TCP echo server and send one message."""

import argparse
import socket


def echo_client(host, port, message):
    """Send a message to the echo server and print its response."""
    with socket.create_connection((host, port)) as client:
        client.sendall(message.encode("utf-8"))
        response = client.recv(2048)

    print(f"Echo from server: {response.decode('utf-8', errors='replace')}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="TCP Echo Client")
    parser.add_argument("--host", default="127.0.0.1", help="server host (default: 127.0.0.1)")
    parser.add_argument("--port", type=int, default=5000, help="server port (default: 5000)")
    parser.add_argument("message", nargs="?", help="message to send; prompts if omitted")
    args = parser.parse_args()

    message = args.message if args.message is not None else input("Message to send: ")
    try:
        echo_client(args.host, args.port, message)
    except ConnectionRefusedError:
        raise SystemExit(
            f"Could not connect to {args.host}:{args.port}. "
            f"Start the server first with: python TCPEcho.py --port {args.port}"
        ) from None
