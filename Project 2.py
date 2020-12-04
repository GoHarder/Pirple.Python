from random import choice

# Game data
lib = [
    'potato',
    'orange',
    'dog',
    'chair',
    'horse',
    'monkey',
    'cake'
]
temp = ''
board = []
parts = 0


def makeBoard(word):
    out = []
    for letter in word:
        obj = {'char': letter, 'show': False}
        out.append(obj)
    return out


def guess(letter):
    global parts
    fail = True
    for i in board:
        if i['char'] == letter:
            i['show'] = True
            fail = False
    if fail:
        parts += 1


def checkWin(board):
    out = True
    for i in board:
        if i['show'] == False:
            out = False
    return out


def printMan(parts):
    man = [' ', 'o', ' ', '\n', '/', '|', u'\u2216', '\n' '/', ' ', u'\u2216']
    out = ''
    r = 0

    if parts == 1:
        r = 3
    elif parts == 2:
        r = 5
    elif parts == 3:
        r = 6
    elif parts == 4:
        r = 7
    elif parts == 5:
        r = 8
    elif parts == 6:
        r = 10
    else:
        r = 0

    for i in range(r):
        out += man[i]
    print(out)


def printBoard(board):
    out = ''
    for i in board:
        c = '_'
        if i['show']:
            c = i['char']
        c += ' '
        out += c
    print(out)


for i in range(len(lib)):
    print(i + 1, lib[i])

while len(board) == 0:
    print('\nPlayer 1 select a word:')
    temp = int(input('> '))
    if temp - 1 in range(len(lib)):
        board = makeBoard(lib[temp - 1])
        print(chr(27) + "[2J")
        break
    else:
        print('Error: Not a valid selection.')

while True:
    printMan(parts)
    printBoard(board)
    print('\nPlayer 2 select a letter:')
    letter = input('> ')
    print('\n')
    guess(letter)
    if checkWin(board):
        printBoard(board)
        print('\nPlayer 2 wins')
        break
    elif parts == 6:
        printMan(parts)
        print('\nPlayer 1 wins')
        break
