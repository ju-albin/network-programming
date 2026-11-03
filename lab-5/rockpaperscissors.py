import socket

def serversideGetPlaySocket():
    pass

def clientsideGetPlaySocket(host):
    pass


ans = "?"

while ans not in {"C", "S"}:
    ans = input("Do you want to be server (S) or client (C): ").upper()