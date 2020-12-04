from random import shuffle


def colR(string):
    return '\u001b[91m' + string + '\u001b[0m'


class Deck:
    def __init__(self):
        self.suits = [u'\u2664', u'\u2665', u'\u2666', u'\u2667']
        self.values = ['A', '2', '3', '4', '5', '6',
                       '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = self.stack()
        self.length = 0

    def stack(self):
        self.cards = []
        self.length = 52
        for suit in self.suits:
            for card in self.values:
                self.cards.append(suit + '-' + card)
        return self.cards

    def shuffle(self):
        self.chart = self.cards.copy()
        shuffle(self.cards)

    def dealCard(self):
        if len(self.cards) != 0:
            card = self.cards[0]
            self.cards.remove(card)
            self.length -= 1
            return card
        return False

    def dealCards(self, length):
        if length <= self.length:
            out = []
            for i in range(length):
                card = self.dealCard()
                out.append(card)
            return out
        else:
            return False
