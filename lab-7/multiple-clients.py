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
                s.sendAll(message.encode())
                
    else:
        data = sock.recv(2048)
        if not data:
            ip, port = sock.getpeername()
            message = f"[{ip}:{port}] (disconnected)"
            for s in listOfSockets:
                if s != sockL and s != sock:
                    s.sendAll(message.encode())
            print(f"Connection from {sock.getpeername()} closed.")
            listOfSockets.remove(sock)
            sock.close()