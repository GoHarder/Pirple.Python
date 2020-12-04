# Testing hands
suits = [u'\u2660', u'\u2661', u'\u2662', u'\u2663']
s = suits[0]
h = suits[1]
d = suits[2]
c = suits[3]
hands = [
    ['Royal Flush', [h + '-A', h + '-K', h + '-Q', h + '-J', h + '-10']],
    ['Straight Flush', [h + '-A', h + '-2', h + '-3', h + '-4', h + '-5']],
    ['Four of a Kind', [h + '-7', d + '-7', c + '-7', s + '-7', h + '-9']],
    ['Full House', [d + '-2', s + '-2', h + '-2', c + '-8', h + '-8']],
    ['Flush', [h + '-3', h + '-7', h + '-9', h + '-J', h + '-K']],
    ['Straight', [h + '-K', c + '-Q', h + '-J', d + '-10', s + '-9']],
    ['Three of a Kind', [d + '-2', s + '-2', h + '-2', c + '-K', h + '-8']],
    ['Tow Pair', [d + '-10', s + '-10', h + '-5', c + '-5', d + '-3']],
    ['One Pair', [d + '-7', s + '-7', h + '-5', c + '-6', d + '-3']],
    ['High Card', [d + '-7', s + '-8', h + '-5', c + '-J', h + '-K']]
]
