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