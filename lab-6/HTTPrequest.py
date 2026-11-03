import socket

PORT = 8080

server = socket.socket(
    socket.AF_INET, 
    socket.SOCK_STREAM
)

server.setsockopt(socket.SOL_SOCKET, 
    socket.SO_REUSEADDR, 
    1
)

server.bind(("", PORT))
server.listen()

print(f"Listening on port {PORT}...")

while True:
    clientSocket, address = server.accept()
    print(f"Connection from {address} established.")
    data = clientSocket.recv(1024)

    request = data.decode("ASCII")
    print(f"Request: {request}")
    clientSocket.sendall(b"HTTP/1.1 200 OK\r\n")
    clientSocket.sendall(b"Content-Type: text/html\r\n")
    clientSocket.sendall(b"\r\n")
    clientSocket.sendall(
        bytearray(
            """
            <html>
            <body>
            <pre>{}</pre>
            </body>
            </html>
            """.format(request),
            "ASCII"
        )
    )
    clientSocket.close()
