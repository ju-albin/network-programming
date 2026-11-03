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

def getWinner(play, otherPlay):
    if (play == otherPlay):
        return 0

    if ((play == "R" and otherPlay == "S") or 
        (play == "S" and otherPlay == "P") or
        (play == "P" and otherPlay == "R")):
        return 1

    return -1

def printWinner(winner):
    if (winner == 0):
        print("It's a tie!")
    elif (winner == 1):
        print("You win!")
    else:
        print("You lose!")

def getMove():
    move = "?"

    while move not in {"R", "P", "S"}:
        move = input("Enter your play (R, P, S): ").upper()

    return move

ans = "?"

while ans not in {"C", "S"}:
    ans = input("Do you want to be server (S) or client (C): ").upper()

if (ans == "S"):
    sock = serversideGetPlaySocket()
else:
    host = input("Enter the server's name or IP address: ")
    sock = clientsideGetPlaySocket(host)

print("Connected to the other player. Let's play!")

if (ans == "S"):
    print("You are player 1 and will play first.")
else:
    print("You are player 2 and will play second.")



myScore = 0
otherScore = 0

if (ans == "S"):
    while myScore < 10 and otherScore < 10:
        play = getMove()
        sock.send(play.encode())
        otherPlay = sock.recv(1024).decode("ASCII")
        winner = getWinner(play, otherPlay)
        if winner == 1:
            myScore += 1
        elif winner == -1:
            otherScore += 1
        printWinner(winner)
        print("The other player played: {}".format(otherPlay))
else:
    while myScore < 10 and otherScore < 10:
        otherPlay = sock.recv(1024).decode("ASCII")
        print("The other player played: {}".format(otherPlay))
        play = getMove()
        sock.send(play.encode())
        winner = getWinner(play, otherPlay)
        if winner == 1:
            myScore += 1
        elif winner == -1:
            otherScore += 1
        printWinner(winner)

if myScore == 10:
    print(f"You won {myScore} against {otherScore}")
else:
    print(f"You lost with {myScore} against {otherScore}")
