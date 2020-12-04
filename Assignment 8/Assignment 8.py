# Imports
import os


# Program data
State = 'main'
TempState = ''
FileName = ''
File = ''


# Graphics
def printMain():
    print('\nPython Notes')
    print('=============================')
    print('--new, --file, --help, --quit')


def printNew():
    print('\nNew')
    print('======================')
    print('--back, --help, --quit')


def printFile():
    print('\nFile')
    print('================================================')
    print('--open, --edit, --delete, --back, --help, --quit')


def printHelp():
    print('\nHelp')
    if TempState == 'main':
        print('==========================')
        print('Key      Description')
        print('--------------------------')
        print('--new    Create a new file')
        print('--file   Open file menu')
        print('--help   Open help menu')
        print('--quit   Quit to terminal')
    elif TempState == 'new':
        print('==========================')
        print('Key      Description')
        print('--------------------------')
        print('--back   Back to main Menu')
        print('--help   Open help menu')
        print('--quit   Quit to terminal')
    elif TempState == 'file':
        print('============================')
        print('Key        Description')
        print('----------------------------')
        print('--open     Open a file')
        print('--edit     Append the file')
        print('--delete   Delete a file')
        print('--back     Back to main Menu')
        print('--help     Open help menu')
        print('--quit     Quit to terminal')
    else:
        print('==========================')
        print('Key      Description')
        print('--------------------------')
        print('--back   Back to file Menu')
        print('--help   Open help menu')
        print('--quit   Quit to terminal')


def printDir(label):
    data = os.listdir('./data')
    display = []
    width = 6

    if len(label) > width:
        width = len(label)

    for note in data:
        line = note.split('.')[0]
        print(line)
        display.append(line)
        if len(line) > width:
            width = len(line)

    print('\n' + label)
    print('=' * width)
    print('--back\n')

    print('Files')
    print('-' * width)
    for line in display:
        print(line)


# Program cli
def _main():
    global State
    global TempState
    printMain()

    while True:
        print('\nSelect:')
        cmd = input('> ')

        if cmd in ['--new', '-n']:
            State = 'new'
            break
        elif cmd in ['--file', '-f']:
            State = 'file'
            break
        elif cmd in ['--help', '-h']:
            State = 'help'
            TempState = 'main'
            break
        elif cmd in ['--quit', '-q']:
            State = ''
            break
        else:
            print('\nError: Command \'' + cmd + '\' does not exist')
            print('Enter \'--help\' for command list')


def _new():
    global State
    global TempState
    global FileName
    global File

    printNew()
    print('\nFile name:')
    cmd = input('> ')

    if cmd in ['--back', '-b']:
        State = 'main'
    elif cmd in ['--help', '-h']:
        State = 'help'
        TempState = 'new'
    elif cmd in ['--quit', '-q']:
        State = ''
    else:
        data = os.listdir('./data')
        FileName = cmd + '.txt'
        if FileName in data:
            print('\nError: File \'' + cmd + '\' already exists')
            print('Enter \'--help\' for command list')
            FileName = ''
        else:
            File = open('./data/' + FileName, 'w')
            State = 'edit'


def _file():
    global State
    global TempState
    global FileName
    global File
    data = os.listdir('./data')

    printFile()
    print('\nSelect:')
    cmd = input('> ')

    if cmd in ['--open', '-o']:
        printDir('Open')
        print('\nSelect:')
        subCmd = input('> ')
        FileName = subCmd + '.txt'

        if subCmd in ['--back', '-b']:
            FileName = ''
            State = 'file'
        elif FileName in data:
            File = open('./data/' + FileName, 'r')
            State = 'read'
        else:
            print('\nError: Command or file does not exist')
            FileName = ''
            State = 'file'
    elif cmd in ['--edit', '-e']:
        printDir('Edit')
        print('\nSelect:')
        subCmd = input('> ')
        FileName = subCmd + '.txt'

        if subCmd in ['--back', '-b']:
            FileName = ''
            State = 'file'
        elif FileName in data:
            File = open('./data/' + FileName, 'r+')
            State = 'edit'
        else:
            print('\nError: Command or file does not exist')
            FileName = ''
            State = 'file'
    elif cmd in ['--delete', '-d']:
        printDir('Delete')
        print('\nSelect:')
        subCmd = input('> ')
        FileName = subCmd + '.txt'

        if subCmd in ['--back', '-b']:
            FileName = ''
            State = 'file'
        elif FileName in data:
            os.remove('./data/' + FileName)
            FileName = ''
        else:
            print('\nError: Command or file does not exist')
            FileName = ''
            State = 'file'
    elif cmd in ['--back', '-b']:
        State = 'main'
    elif cmd in ['--help', '-h']:
        State = 'help'
        TempState = 'file'
    elif cmd in ['--quit', '-q']:
        State = ''
    else:
        print('\nError: Command \'' + cmd + '\' does not exist')
        print('Enter \'--help\' for command list')


def _read():
    global State
    global FileName
    title = FileName.split('.')[0]
    print('\n' + title)
    print('-' * len(title))

    lines = File.readlines()

    for line in lines:
        print(line.rstrip('\n'))

    File.close()
    FileName = ''
    print('\nPress any key to continue:')
    cmd = input('> ')
    State = 'file'


def _edit():
    global State
    global TempState
    global FileName
    title = FileName.split('.')[0]
    lines = File.readlines()
    print('\nEdit')
    print('======================')
    print('--close --help, --quit')
    print('\n' + title)
    print('-' * len(title))

    for line in lines:
        print(line.rstrip('\n'))

    while True:
        cmd = input('> ')

        if cmd in ['--close', '-c']:
            State = 'file'
            File.close()
            FileName = ''
            break
        elif cmd in ['--help', '-h']:
            State = 'help'
            TempState = 'edit'
            break
        elif cmd in ['--quit', '-q']:
            State = ''
            File.close()
            FileName = ''
            break
        else:
            File.write('\n' + cmd)


def _help():
    global State
    global TempState
    printHelp()
    print('\nPress any key to continue:')
    cmd = input('> ')
    State = TempState
    TempState = ''


while State != '':
    if State == 'main':
        _main()
    elif State == 'new':
        _new()
    elif State == 'file':
        _file()
    elif State == 'read':
        _read()
    elif State == 'edit':
        _edit()
    elif State == 'help':
        _help()
    else:
        break
