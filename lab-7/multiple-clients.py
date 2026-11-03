import socket
import select

HOST = "localhost"
PORT = 12345

sockL = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockL.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sockL.bind((HOST, PORT))
sockL.listen(5)

listOfSockets = [sockL]

print (f"Server listening on {HOST}:{PORT}")

while True:

    ready, _, _ = select.select(
        listOfSockets,
        [],
        []
    )

    sock = ready[0]

    if sock == sockL:
        sockClient, addr = sockL.accept()
        listOfSockets.append(sockClient)
        print(f"Connection from {addr} established.")
        
        ip, port = addr
        message = f"[{ip}:{port}] (connected)"
        for s in listOfSockets:
            if s != sockL and s != sockClient:
                s.sendall(message.encode())
                
    else:
        data = sock.recv(2048)
        if not data:
            ip, port = sock.getpeername()
            message = f"[{ip}:{port}] (disconnected)"
            for s in listOfSockets:
                if s != sockL and s != sock:
                    s.sendall(message.encode())
            print(f"Connection from {sock.getpeername()} closed.")
            listOfSockets.remove(sock)
            sock.close()
        else:
            ip, port = sock.getpeername()
            
            message = f"[{ip}:{port}] {data.decode('ASCII')}"
            for s in listOfSockets:
                if s != sockL:
                    s.sendall(message.encode())