# Experiment 11: UDP client
# Run after the server:  python3 udp_client.py
# Optional: python3 udp_client.py <server_ip>
import socket
import sys

HOST = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
PORT = 8080


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)    # create UDP socket
    client.settimeout(3)                                         # UDP has no delivery guarantee
    print(f"[UDP Client] Sending to {HOST}:{PORT}. Type 'exit' to quit.")
    try:
        while True:
            msg = input("You: ")
            if msg.strip().lower() == "exit":
                break
            client.sendto(msg.encode(), (HOST, PORT))            # no connect() needed
            try:
                reply, _ = client.recvfrom(1024)
                print(f"Server: {reply.decode()}")
            except socket.timeout:
                print("No reply (datagram or reply may have been lost)")
    except (KeyboardInterrupt, EOFError):
        pass
    finally:
        client.close()
        print("[UDP Client] Socket closed")


if __name__ == "__main__":
    main()
