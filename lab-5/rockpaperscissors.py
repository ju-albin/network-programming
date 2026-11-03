import socket

def serversideGetPlaySocket():
    server = socket.socket(
        socket.AF_INET, 
        socket.SOCK_STREAM
    )
    server.bind(('', 60003))

    server.listen()

    clientSocket, addr = server.accept()

    return clientSocket

def clientsideGetPlaySocket(host):
    client = socket.socket(
        socket.AF_INET, 
        socket.SOCK_STREAM
    )
    client.connect((host, 60003))

    return client


ans = "?"

while ans not in {"C", "S"}:
    ans = input("Do you want to be server (S) or client (C): ").upper()

if (ans == "S"):
    sock = serversideGetPlaySocket()
else:
    host = input("Enter the server's name or IP address: ")
    sock = clientsideGetPlaySocket(host)

print("Connected to the other player. Let's play!")