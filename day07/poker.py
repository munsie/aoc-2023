#!/usr/bin/env python3

import collections
import enum
import functools
import pprint

import sys
sys.path.append('../common')

RANKS = [ 'A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2' ]

class HandTypes(enum.IntEnum):
    FIVE_OF_A_KIND = 6
    FOUR_OF_A_KIND = 5
    FULL_HOUSE = 4
    THREE_OF_A_KIND = 3
    TWO_PAIR = 2
    ONE_PAIR = 1
    HIGH_CARD = 0

def hand_type(hand) -> HandTypes:
    counts = collections.Counter(hand).most_common()
    if counts[0][1] == 5:
        return HandTypes.FIVE_OF_A_KIND
    elif counts[0][1] == 4:
        return HandTypes.FOUR_OF_A_KIND
    elif counts[0][1] == 3 and counts[1][1] == 2:
        return HandTypes.FULL_HOUSE
    elif counts[0][1] == 3:
        return HandTypes.THREE_OF_A_KIND
    elif counts[0][1] == 2 and counts[1][1] == 2:
        return HandTypes.TWO_PAIR
    elif counts[0][1] == 2:
        return HandTypes.ONE_PAIR
    else:
        return HandTypes.HIGH_CARD
    
def compare_hand(h1, h2):
    # first check to see if the hand type alone is enough
    if int(h1[2]) < int(h2[2]):
        return -1
    elif int(h1[2]) > int(h2[2]):
        return 1
    else:
        # we have a tie -- we have to look at the individual cards to see which one is higher for each position
        for i in range(len(h1[0])):
            r1 = RANKS.index(h1[0][i])
            r2 = RANKS.index(h2[0][i])
            if r1 < r2:
                return 1
            elif r1 > r2:
                return -1
        return 0

if __name__ == '__main__':
    with open('input.txt') as f:
        hands = [l.split() for l in f]

    # calculate all of the hand types
    for hand in hands:
        hand.append(hand_type(hand[0]))

    # sort them in order from worst to best hand
    hands.sort(key=functools.cmp_to_key(compare_hand))

    # calculate our winnings
    winnings = 0
    for h in range(len(hands)):
        winnings += int(hands[h][1]) * (h + 1)
        
    print(winnings)
