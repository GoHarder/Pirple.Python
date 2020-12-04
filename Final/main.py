from playingcards import Deck
from pokerplayer import Player
from time import sleep

state = 'main'
temp = ''
player = None
deck = Deck()
X = u'\u25a0'


# Colors
def colR(string):
    return '\u001b[91m' + string + '\u001b[0m'


def colG(string):
    return '\u001b[32m' + string + '\u001b[0m'


def render(text):
    print('')
    for line in text:
        print(line)
    print('')


def getCmd(prompt):
    print(prompt)
    return input('> ')


def setState(new):
    global state
    global temp
    temp = state
    state = new


def back():
    global state
    global temp
    state = temp
    temp = ''


def run(cmd, routes):
    search = None
    for route in routes:
        if cmd in route[0]:
            search = route

    last = routes[len(routes) - 1]
    if 'else' in last[0] and search == None:
        search = last

    if search != None:
        go = search[1]
        if len(search) == 3:
            var = search[2]
            go(var)
        else:
            go()
    else:
        print('\nError: Command doesn\'t exist.')


def sMain():
    text = [
        X + '-' * 13 + X,
        '| Video Poker |',
        X + '-' * 13 + X,
        '|   --start   |',
        '|   --help    |',
        '|   --quit    |',
        X + '-' * 13 + X,
    ]
    render(text)

    cmd = getCmd('Select:')

    routes = [
        [['--start', '-s'], setState, 'start'],
        [['--help', '-h'], setState, 'help'],
        [['--quit', '-q'], setState, '']
    ]
    run(cmd, routes)


def sStart():
    cmd = getCmd('\nEnter your name:')

    def cElse(cmd):
        global player
        if len(cmd) > 0:
            player = Player(cmd)
            setState('bet')

    routes = [
        [['--help', '-h'], setState, 'help'],
        [['--quit', '-q'], setState, ''],
        [['else'], cElse, cmd]
    ]
    run(cmd, routes)


def sBet():
    global player
    string = '${:,.2f}'.format(player.money)
    print('\n' + player.name + '\'s money = ' + colG(string))
    cmd = getCmd('Place bet:')

    def cElse(cmd):
        global player

        try:
            cmd = float(cmd)
        except:
            print('\nError: Enter an amount.')
            cmd = 0

        bet = player.placeBet(cmd)

        if bet:
            setState('deal')
        else:
            cmd = None

    routes = [
        [['--help', '-h'], setState, 'help'],
        [['--quit', '-q'], setState, ''],
        [['else'], cElse, cmd]
    ]
    run(cmd, routes)


def sDeal():
    global player
    global deck

    if deck.length < 10:
        deck.stack()

    if deck.length == 52:
        deck.shuffle()

    # print('\n' + colR('Length ' + str(deck.length)))

    player.getHand(deck.dealCards(5))
    print('')
    print(player)
    cmd = getCmd('\nSelect cards to discard or --done to continue:')

    def cElse(cmd):
        global player
        try:
            cmd = int(cmd)
        except:
            print('\nError: Enter a card.')
            cmd = 0

        if type(cmd) is int:
            player.pick(cmd)

    routes = [
        [['--done', '-d'], setState, 'end'],
        [['--help', '-h'], setState, 'help'],
        [['--quit', '-q'], setState, ''],
        [['else'], cElse, cmd]
    ]
    run(cmd, routes)


def sEnd():
    global player
    global deck

    newCards = deck.dealCards(len(player.discards))
    player.switch(newCards)

    print('')
    print(player)

    payTable = {
        'Royal Flush': 250,
        'Straight Flush': 50,
        'Four of a Kind': 25,
        'Full House': 9,
        'Flush': 6,
        'Straight': 4,
        'Three of a Kind': 3,
        'Two Pair': 2,
        'One Pair': 1,
        'High Card': 0
    }
    pay = payTable.get(player.rank, 0)
    winnings = round(pay * player.bet, 2)

    if pay == 0:
        print('\n' + colR('You Lose!'))
    else:
        string = '${:,.2f}'.format(winnings)
        print('\nYou Win! ' + colG(string))

    player.reset()
    player.getMoney(winnings)

    if player.money < 1:
        text = [
            X + '-' * 11 + X,
            '| ' + colR('Game Over') + ' |',
            X + '-' * 11 + X,
        ]
        render(text)
        sleep(2)
        setState('')
    else:
        sleep(1)
        setState('bet')


def sHelp():
    global temp
    main = [
        X + '-' * 25 + X,
        '| Help                    |',
        X + '-' * 25 + X,
        '| Command   Description   |',
        '|' + '-' * 25 + '|',
        '| --start   Start program |',
        '| --help    Open help     |',
        '| --quit    Quit program  |',
        X + '-' * 25 + X,
    ]

    start = [
        X + '-' * 24 + X,
        '| Help                   |',
        X + '-' * 24 + X,
        '| Prompt                 |',
        '|' + '-' * 24 + '|',
        '| Input your name        |',
        X + '-' * 24 + X,
        '| Command   Description  |',
        '|' + '-' * 24 + '|',
        '| --help    Open help    |',
        '| --quit    Quit program |',
        X + '-' * 24 + X,
    ]

    bet = [
        X + '-' * 38 + X,
        '| Help                                 |',
        X + '-' * 38 + X,
        '| Prompt                               |',
        '|' + '-' * 38 + '|',
        '| Enter a float for x (0 < X <= money) |',
        X + '-' * 38 + X,
        '| Command   Description                |',
        '|' + '-' * 38 + '|',
        '| --help    Open help                  |',
        '| --quit    Quit program               |',
        X + '-' * 38 + X,
    ]

    deal = [
        X + '-' * 45 + X,
        '| Help                                        |',
        X + '-' * 45 + X,
        '| Prompt                                      |',
        '|' + '-' * 45 + '|',
        '| Select a card 1 - 5 and mark it for discard |',
        X + '-' * 45 + X,
        '| Command   Description                       |',
        '|' + '-' * 45 + '|',
        '| --done    Get new cards                     |',
        '| --help    Open help                         |',
        '| --quit    Quit program                      |',
        X + '-' * 45 + X,
    ]

    routes = {
        'main': main,
        'start': start,
        'bet': bet,
        'deal': deal,
    }

    text = routes.get(temp, ['Error: No text'])

    render(text)

    getCmd('Press any key to continue:')

    text = [
        X + '-' * 43 + X,
        '| Video Poker                               |',
        X + '-' * 43 + X,
        '| 1. Place your bet                         |',
        '| 2. Get cards                              |',
        '| 3. Select which cards you want to discard |',
        '| 4. Get more cards                         |',
        '| 5. Win based on hand                      |',
        X + '-' * 43 + X
    ]

    render(text)

    getCmd('Press any key to continue:')

    text = [
        X + '-' * 33 + X,
        '| Video Poker                     |',
        X + '-' * 33 + X,
        '| Hand             Win multiplier |',
        '|' + '-' * 33 + '|',
        '| Royal Flush      x250           |',
        '| Straight Flush   x50            |',
        '| Four of a Kind   x25            |',
        '| Full House       x9             |',
        '| Flush            x6             |',
        '| Straight         x4             |',
        '| Three of a Kind  x3             |',
        '| Two Pair         x2             |',
        '| One Pair         x1             |',
        '| High Card        x0             |',
        X + '-' * 33 + X,
    ]

    render(text)

    cmd = getCmd('Enter --resume to continue:')

    routes = [
        [['--resume', '-r'], back],
        [['--quit', '-q'], setState, ''],
    ]
    run(cmd, routes)


routes = {
    'main': sMain,
    'start': sStart,
    'bet': sBet,
    'deal': sDeal,
    'end': sEnd,
    'help': sHelp
}

while state != '':
    go = routes.get(state, None)
    if go != None:
        go()
    else:
        state = ''
