# Experiment 11: TCP client
# Run after the server:  python3 tcp_client.py
# Optional: python3 tcp_client.py <server_ip>
import socket
import sys

HOST = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
PORT = 7070


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    # create
    client.connect((HOST, PORT))                                  # connect
    print(f"[Client] Connected to {HOST}:{PORT}. Type 'exit' to quit.")
    try:
        while True:
            msg = input("You: ")
            if msg.strip().lower() == "exit":
                break
            client.send(msg.encode())                             # send
            reply = client.recv(1024).decode()                    # receive
            print(f"Server: {reply}")
    except (KeyboardInterrupt, EOFError):
        pass
    finally:
        client.close()                                            # close
        print("[Client] Connection closed")


if __name__ == "__main__":
    main()
