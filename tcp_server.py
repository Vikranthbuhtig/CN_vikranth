# Experiment 11: Multi-client TCP echo server
# Run first:  python3 tcp_server.py
import socket
import threading

HOST = "127.0.0.1"   # use "0.0.0.0" to accept clients from other computers
PORT = 7070


def handle_client(conn, addr):
    print(f"[Server] Client connected from {addr[0]}:{addr[1]}")
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:                      # empty data = client closed
                break
            msg = data.decode()
            print(f"[Server] Received from {addr[1]}: {msg}")
            conn.send(f"Echo from server: {msg}".encode())
    print(f"[Server] Client {addr[1]} disconnected")


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    # create
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))                                     # bind
    server.listen(5)                                              # listen
    print(f"[Server] Listening on {HOST}:{PORT}  (press Ctrl+C to stop)")
    try:
        while True:
            conn, addr = server.accept()                          # accept
            threading.Thread(target=handle_client, args=(conn, addr),
                             daemon=True).start()
    except KeyboardInterrupt:
        print("\n[Server] Shutting down")
    finally:
        server.close()


if __name__ == "__main__":
    main()
