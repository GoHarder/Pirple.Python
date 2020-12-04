# Program data
state = 'main'
tempState = ''

# Game data
player = 1
playerName = 'Black'
chip = u'\u2B24'
board = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
]

# Lines
h = u'\u2500'
v = u'\u2502'
tL = u'\u250c'
tR = u'\u2510'
bL = u'\u2514'
bR = u'\u2518'
lT = u'\u2520'
rT = u'\u2528'


def hLine(length):
    out = ''
    for i in range(length):
        out += h
    return out


# Colors
def colY(string):
    return '\u001b[93m' + string + '\u001b[0m'


def colR(string):
    return '\u001b[91m' + string + '\u001b[0m'


def colG(string):
    return '\u001b[32m' + string + '\u001b[0m'


# Graphics
def printBoard():
    print(colY(tL + ' 1 2 3 4 5 6 7 ' + tR))
    for row in board:
        out = colY(v + ' ')
        for cell in row:
            cellStr = ' '
            if cell == 1:
                cellStr = chip
            elif cell == 2:
                cellStr = colR(chip)
            out += cellStr + ' '
        out += colY(v)
        print(out)
    print(colY(bL + hLine(15) + bR))
    print('\n' + playerName + '\'s turn:\n')


def printMain():
    print(colY(tL + hLine(11) + tR))
    print(colY(v) + ' Connect 4 ' + colY(v))
    print(colY(lT + hLine(11) + rT))
    print(colY(v) + '   start   ' + colY(v))
    print(colY(v) + '   help    ' + colY(v))
    print(colY(v) + '   quit    ' + colY(v))
    print(colY(bL + hLine(11) + bR))
    print('\nSelect command:\n')


def printHelp():
    print(colY(tL + hLine(30) + tR))
    print(colY(v) + ' Commands                     ' + colY(v))
    print(colY(lT + hLine(30) + rT))
    print(colY(v) + ' Key     Description          ' + colY(v))
    print(colY(v + ' ' + hLine(28) + ' ' + v))
    print(colY(v) + ' 1 - 7   Put chip in column   ' + colY(v))
    print(colY(v) + ' reset   Reset game           ' + colY(v))
    print(colY(v) + ' help    Open help menu       ' + colY(v))
    print(colY(v) + ' quit    Exit to command line ' + colY(v))
    print(colY(bL + hLine(30) + bR))
    print('\nPress any key to continue:\n')


# Game functions
def changeTurn():
    global player
    global playerName

    if player == 1:
        player = 2
        playerName = 'Red'
    else:
        player = 1
        playerName = 'Black'


def reset():
    global player
    global playerName
    player = 1
    playerName = 'Black'

    for i in range(len(board)):
        row = board[i]
        for i in range(len(row)):
            row[i] = 0


def move(col):
    for i in range(len(board)):
        cell = board[5 - i][col - 1]
        if cell == 0:
            board[5 - i][col - 1] = player
            return True
    return False


def checkWin():
    tempBoard1 = []
    tempBoard2 = []
    tempBoard3 = []

    # Rotates board 90 deg
    for i in range(7):
        outRow = []
        for row in board:
            outRow.append(row[i])
        tempBoard1.append(outRow)
    # Rotates board 45 deg
    for i1 in range(3):
        for i2 in range(4):
            outRow = []
            for i3 in range(4):
                outRow.append(board[i1 + i3][i2 + i3])
            tempBoard2.append(outRow)
    # Rotates board -45 deg
    for i1 in range(3):
        for i2 in range(4):
            outRow = []
            for i3 in range(4):
                outRow.append(board[i1 + i3][(6 - i2) - i3])
            tempBoard3.append(outRow)
    # Checks each 4 in row
    for i1 in range(len(board)):
        for i2 in range(4):
            check = set(board[i1][i2:i2 + 4])
            if len(check) == 1:
                if 1 in check or 2 in check:
                    return True
    # Checks each 4 in column
    for i1 in range(len(tempBoard1)):
        for i2 in range(3):
            check = set(tempBoard1[i1][i2:i2 + 4])
            if len(check) == 1:
                if 1 in check or 2 in check:
                    return True
    # Checks each 4 in diag1
    for i1 in range(len(tempBoard2)):
        check = set(tempBoard2[i1])
        if len(check) == 1:
            if 1 in check or 2 in check:
                return True
    # Checks each 4 in diag2
    for i1 in range(len(tempBoard3)):
        check = set(tempBoard3[i1])
        if len(check) == 1:
            if 1 in check or 2 in check:
                return True
    return False


# Game cli
def _main():
    global state
    global tempState
    printMain()

    while True:
        cmd = input('> ')

        if cmd == 'start':
            state = 'game'
            break
        elif cmd == 'help':
            state = 'help'
            tempState = 'main'
            break
        elif cmd == 'quit':
            state = ''
            break
        else:
            print(colR('ERROR: ') +
                  'Command does not exist enter \'help\' for assistance')


def _game():
    global state
    global tempState

    while True:
        printBoard()
        cmd = input('> ')

        if cmd == 'help':
            state = 'help'
            tempState = 'game'
            break
        elif cmd == 'quit':
            state = ''
            break
        elif cmd == 'reset':
            reset()
        else:
            try:
                col = int(cmd)

                if cmd - 1 in range(7):
                    go = move(col)

                    if go:
                        win = checkWin()

                        if win:
                            reset()
                            print(colG(playerName + ' wins!'))
                        else:
                            changeTurn()
                    else:
                        print(colR('ERROR: ') + 'Column is full')
                else:
                    break
            except:
                print(colR('ERROR: ') +
                      'Command' + cmd + 'does not exist enter \'help\' for assistance')


def _help():
    global state
    global tempState
    printHelp()
    cmd = input('> ')
    state = tempState
    tempState = ''


while state != '':
    if state == 'main':
        _main()
    elif state == 'game':
        _game()
    elif state == 'help':
        _help()
    else:
        break
