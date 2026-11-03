import socket

POINTS_BEFORE_WIN = 10
PORT = 60003


def serversideGetPlaySocket():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server.bind(("", PORT))
    server.listen()

    clientSocket, _ = server.accept()
    return clientSocket


def clientsideGetPlaySocket(host):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client.connect((host, PORT))
    return client


def getMove():
    move = "?"

    while move not in {"R", "P", "S"}:
        move = input("Enter your play (R, P, S): ").upper()

    return move


def getWinner(play, otherPlay):
    if play == otherPlay:
        return 0

    if (
        (play == "R" and otherPlay == "S")
        or (play == "S" and otherPlay == "P")
        or (play == "P" and otherPlay == "R")
    ):
        return 1

    return -1


def printWinner(winner):
    if winner == 0:
        print("It's a tie!")
    elif winner == 1:
        print("You win!")
    else:
        print("You lose!")



ans = "?"

while ans not in {"C", "S"}:
    ans = input("Do you want to be server (S) or client (C): ").upper()

if ans == "S":
    sock = serversideGetPlaySocket()
else:
    host = input("Enter the server's name or IP address: ")
    sock = clientsideGetPlaySocket(host)

print("Connected to the other player. Let's play!")



## Start with 0 points for both players
myScore = 0
otherScore = 0


while myScore < POINTS_BEFORE_WIN and otherScore < POINTS_BEFORE_WIN:

    print(f"({myScore},{otherScore}) Your move:")

    play = getMove()

    sock.send(play.encode())

    otherPlay = sock.recv(1024).decode("ASCII")

    print(f"(opponent's move: {otherPlay})")

    winner = getWinner(play, otherPlay)

    if winner == 1:
        myScore += 1
    elif winner == -1:
        otherScore += 1

    printWinner(winner)




if myScore == POINTS_BEFORE_WIN:
    print(f"You won {myScore} against {otherScore}")
else:
    print(f"You lost with {myScore} against {otherScore}")

sock.close()
