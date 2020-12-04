import random as r
import time as t
import math as m

# --------------
# Random
# --------------

# from random import * #loads in everything like above
# from random import randint, random, uniform, shuffle #pick which functions you want

test1 = r.randint(1, 10)  # start<=n<=end
test2 = r.random()  # 0.0<=n<=1.0
test3 = r.uniform(1, 10)  # start<=n<=end


def playingCards():
    suits = [u'\u2660', u'\u2665', u'\u2666', u'\u2663']
    cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    deck = []

    for suit in suits:
        for card in cards:
            deck.append(suit + card)
    return deck


# deck = playingCards()
# r.shuffle(deck)
# aCard = r.choice(deck)

# --------------
# Math
# --------------
var = 16


sqrt = m.sqrt(var)  # square root
squ = var ** 2  # squared
exp = m.exp(var)  # e ^ 16 e = euler's constant
fact = m.factorial(var)
sin = m.sin(90 * m.pi / 180)  # normal value is in radians
floor = m.floor(1.5)
ceil = m.ceil(1.5)

# --------------
# Time
# --------------
pastTime = t.perf_counter()
print('ping')
print('ping')
print('ping')
currentTime = t.perf_counter()
print(currentTime - pastTime)

# t.sleep(1)  # in seconds like setTimeout
print('go')

# for i in range(10):
#     print(i + 1)
#     t.sleep(1)
