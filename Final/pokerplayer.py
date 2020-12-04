from collections import Counter


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.discards = []
        self.money = 50
        self.bet = 0
        self.rank = self.getRank()

    def __str__(self):
        if self.rank != None:
            out = self.name + '\'s hand = ' + self.rank + '\n'
            row = ''
            p = []
            for card in self.hand:
                if card in self.discards:
                    out += ' X '
                    p.append(' X')
                else:
                    out += card + ' '
                    p.append(card)
            out += '\n'
            for i in range(len(p)):
                length = len(p[i])
                row += ' ' + str(i + 1)
                row += ' ' * (length - 1)
            out += row
            return out
        else:
            return 'Error: Five cards are required for your hand.'

    def pick(self, i):
        if i > 0 and i < 6:
            card = self.hand[i - 1]
            self.discards.append(card)
        else:
            print('\nError: Enter a number between 1 and 5.')

    def switch(self, newCards):
        for i in range(len(newCards)):
            newCard = newCards[i]
            oldCard = self.discards[i]
            self.hand = [newCard if x == oldCard else x for x in self.hand]
        self.rank = self.getRank()

    def getHand(self, hand):
        if len(self.hand) == 0:
            self.hand = hand
            self.rank = self.getRank()

    def reset(self):
        self.hand = []
        self.discards = []
        self.rank = self.getRank()

    def placeBet(self, bet):
        if bet <= self.money and bet != 0:
            bet = round(bet, 2)
            self.bet += bet
            self.money -= bet
            return True
        elif bet == 0:
            print('\nError: You have to bet something.')
            return False
        else:
            print('\nError: You can\'t bet money you don\'t have.')
            return False

    def getMoney(self, money):
        self.bet = 0
        self.money += money

    def getRank(self):
        self.rank = None
        values = []
        suits = []
        if len(self.hand) == 5:
            for card in self.hand:
                card = card.split('-')
                suits.append(card[0])
                values.append(card[1])

            sameSuit = len(set(suits)) == 1
            valueCount = Counter(values)
            groups = []
            for value in values:
                groups.append(valueCount[value])
            groups = set(groups)

            def straight():
                faceLib = {'A': 14, 'K': 13, 'Q': 12, 'J': 11}
                highFace = []

                for value in values:
                    if value in faceLib:
                        n = faceLib[value]
                    else:
                        n = int(value)
                    highFace.append(n)

                lowFace = [x if x < 14 else 1 for x in highFace]

                highFace.sort()
                lowFace.sort()

                for li in [highFace, lowFace]:
                    tests = []
                    for i in range(4):
                        a = li[i]
                        b = li[i + 1]
                        # print(a, b)
                        tests.append(b == a + 1)
                    # print(set(tests))
                    if len(set(tests)) == 1:

                        if tests[0]:
                            return True
                return False

            def royalFlush():
                check = {'A': 1, 'K': 1, 'Q': 1, 'J': 1, '10': 1}
                if valueCount == check and sameSuit:
                    return True
                return False

            def straightFlush():
                if straight() and sameSuit:
                    return True
                return False

            def fourOfaKind():
                if groups == {4, 1}:
                    return True
                return False

            def fullHouse():
                if groups == {3, 2}:
                    return True
                return False

            def flush():
                if sameSuit:
                    return True
                return False

            def threeOfaKind():
                if groups == {3, 1}:
                    return True
                return False

            def twoPair():
                if groups == {2, 1} and len(valueCount) == 3:
                    return True
                return False

            def onePair():
                if groups == {2, 1} and len(valueCount) == 4:
                    return True
                return False

            def highCard():
                return True

            tests = [
                ['Royal Flush', royalFlush],
                ['Straight Flush', straightFlush],
                ['Four of a Kind',  fourOfaKind],
                ['Full House',  fullHouse],
                ['Flush', flush],
                ['Straight', straight],
                ['Three of a Kind',  threeOfaKind],
                ['Two Pair', twoPair],
                ['One Pair', onePair],
                ['High Card', highCard]
            ]

            for test in tests:
                fun = test[1]
                result = fun()
                if result:
                    self.rank = test[0]
                    break
        return self.rank
