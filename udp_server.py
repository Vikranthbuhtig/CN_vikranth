# Experiment 11: UDP (connectionless) echo server
# Run first:  python3 udp_server.py
import socket

HOST = "127.0.0.1"   # use "0.0.0.0" to accept datagrams from other computers
PORT = 8080


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)    # create UDP socket
    server.bind((HOST, PORT))                                    # bind (no listen/accept)
    print(f"[UDP Server] Listening on {HOST}:{PORT}  (press Ctrl+C to stop)", flush=True)
    try:
        while True:
            data, addr = server.recvfrom(1024)                   # receive datagram + sender
            msg = data.decode()
            print(f"[UDP Server] From {addr[0]}:{addr[1]}: {msg}", flush=True)
            server.sendto(f"Echo from UDP server: {msg}".encode(), addr)
    except KeyboardInterrupt:
        print("\n[UDP Server] Shutting down")
    finally:
        server.close()


if __name__ == "__main__":
    main()
