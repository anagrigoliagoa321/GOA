import socket

def start_server():

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.bind(('localhost', 12345))

    server_socket.listen(1)
    print("Server is listening on port 12345...")

    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")

    data = conn.recv(1024)
    print(f"Received: {data.decode()}")

    conn.sendall(b"Hello from server!")
 
    conn.close()

if __name__ == "__main__":
    start_server()

# Client code
import socket

def start_client():

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client_socket.connect(('localhost', 12345))

    client_socket.sendall(b"Hello from client!")

    response = client_socket.recv(1024)
    print(f"Response from server: {response.decode()}")
    
    client_socket.close()

if __name__ == "__main__":
    start_client()