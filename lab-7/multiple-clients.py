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