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
    pass


ans = "?"

while ans not in {"C", "S"}:
    ans = input("Do you want to be server (S) or client (C): ").upper()