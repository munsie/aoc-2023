#!/usr/bin/env python3

import collections
import enum
import functools
import pprint

import sys
sys.path.append('../common')

RANKS = [ 'A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J' ]

class HandTypes(enum.IntEnum):
    FIVE_OF_A_KIND = 6
    FOUR_OF_A_KIND = 5
    FULL_HOUSE = 4
    THREE_OF_A_KIND = 3
    TWO_PAIR = 2
    ONE_PAIR = 1
    HIGH_CARD = 0

def hand_type(hand) -> HandTypes:
    # get a count of all of the cards in the hand
    counts = collections.Counter(hand)
    
    # pull out the count of jokers and then remove it from the counts so we can treat it special
    jokers = counts['J']
    del counts['J']

    # sort the counts by most common
    counts = counts.most_common()

    # hack -- add two empty counts so we don't get an index error below when we only had 5 or 4 jokers
    counts.append(('', 0))
    counts.append(('', 0))

    # figure out what kind of hand this is
    if counts[0][1] + jokers >= 5:
        return HandTypes.FIVE_OF_A_KIND
    elif counts[0][1] + jokers >= 4:
        return HandTypes.FOUR_OF_A_KIND
    # full house has two possibilities:
    #   11122
    #   11J22
    elif counts[0][1] == 3 and counts[1][1] == 2:
        return HandTypes.FULL_HOUSE
    elif counts[0][1] == 2 and counts[1][1] == 2 and jokers == 1:
        return HandTypes.FULL_HOUSE
    elif counts[0][1] + jokers >= 3:
        return HandTypes.THREE_OF_A_KIND
    # two pair has two possibilities
    #   1122x
    #   1J2Jx
    elif counts[0][1] == 2 and counts[1][1] == 2:
        return HandTypes.TWO_PAIR
    elif counts[1][1] == 1 and counts[2][1] == 1 and jokers == 2:
        return HandTypes.TWO_PAIR
    elif counts[0][1] + jokers >= 2:
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
        for c1, c2 in zip(h1[0], h2[0]):
            r1 = RANKS.index(c1)
            r2 = RANKS.index(c2)
            if r1 < r2:
                return 1
            elif r1 > r2:
                return -1
        return 0

if __name__ == '__main__':
    # read in the input
    with open('input.txt') as f:
        hands = []
        for l in f:
            hand = l.split()
            hand[1] = int(hand[1])
            hand.append(hand_type(hand[0]))
            hands.append(hand)

    # sort them in order from worst to best hand
    hands.sort(key=functools.cmp_to_key(compare_hand))

    # calculate our winnings
    winnings = sum([hand[1] * (hands.index(hand) + 1) for hand in hands])   
    print(winnings)
