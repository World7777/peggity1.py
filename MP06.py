#Enci Peng, Eric Allen
import turtle
import random


def drawSquare(t):
    for i in range(4):
        t.forward(1)
        t.left(90)


def drawBoard(numSquares):
    wn = turtle.Screen()
    bob = turtle.Turtle()
    bob.up()
    wn.setworldcoordinates(-2, numSquares+1, numSquares+1, -2)
    wn.tracer(False)
    # drawing rows and columns of squares
    for row in range(numSquares):
        for col in range(numSquares):
            drawSquare(bob)
            bob.forward(1)
        bob.backward(numSquares)
        bob.left(90)
        bob.forward(1)
        bob.right(90)
    # label the board
    bob.speed(0)
    bob.goto(0, 0)
    bob.up()
    bob.forward(.5)
    for col in range(numSquares):
        bob.write(col, align='center', font=('Arial', 16, 'bold'))
        bob.forward(1)
    bob.goto(-.3, 0)
    bob.left(90)
    bob.forward(.8)
    for row in range(numSquares):
        bob.write(chr(row+65), align='center', font=('Arial', 16, 'bold'))
        bob.forward(1)
    wn.tracer(True)
    bob.goto(numSquares//2, -1)
    bob.color("black", "black")
    bob.write("PEGITY", align='center', font=(
        'Lucida Calligraphy', 20, 'bold'))
    bob.ht()
    return bob, wn


def createValidMovesList():
    validMovesList = []
    for row in "ABCDEFGHIJKLMNO":
        for col in range(0, 15):
            validMovesList.append(row+str(col))
    validMovesList.append("QUIT")
    return validMovesList


def drawPeg(t, move, color, validMovesList):
    validMovesList.remove(move)
    row = (ord(move[0]))-65
    col = int(move[1:])
    t.up()
    t.goto(col+1, row+.5)
    t.color(color)
    t.down()
    t.begin_fill()
    t.circle(.5, 360, 360)
    t.end_fill()

def check_win(board):
    n = len(board)
    m = len(board[0])

    for i in range(n):
        for j in range(m):
            row_count = 0
            if j + 6 < m and board[i][j] != None:
                for k in range(j, j + 6):
                    if board[i][j] == board[i][k]:
                        row_count += 1
                    else:
                        break
            col_count = 0
            if i + 6 < n and board[i][j] != None:
                for k in range(i, i + 6):
                    if board[i][j] == board[k][j]:
                        row_count += 1
                    else:
                        break
            if row_count >= 6 or col_count >= 6:
                return board[i][j]

    return None

def main():
    t, scrn = drawBoard(15)
    logical_board = [[None for j in range(15)] for i in range(15)]
    validMovesList = createValidMovesList()
    currentPlayer = ["blue", "green"][random.randint(0, 1)]
    move = ""
    while move != "QUIT":
        move = input("Enter a move "+currentPlayer+" => ").upper()
        while move not in validMovesList:
            move = input("Invalid move!  Enter a valid move " +
                         currentPlayer+" => ").upper()
        if move != "QUIT":
            x = ord(move[0]) - ord('A')
            y = ord(move[1]) - ord('0')
            logical_board[x][y] = currentPlayer
            drawPeg(t, move, currentPlayer, validMovesList)
            winner = check_win(logical_board)
            if  winner != None:
                print('Current winner: ', winner)
                print('Happy playing, bye!')
                move = "QUIT"
        else:
            choice = input('Do you want to save the current game(y/n): ').lower()
            if choice == 'y':
                file = open('game.txt', 'w')
                for row in logical_board:
                    for item in row:
                        file.write(item)
                    file.write('\n')
                file.close()
            print('Happy playing, bye!')
        if currentPlayer == "blue":
            currentPlayer = "green"
        else:
            currentPlayer = "blue"


main()
