#!/usr/bin/env python3

def read_card(s):
    card = {}

    s = " ".join(s.split())

    # read in the card id
    card['id'] = int(s.split(':')[0].split(' ')[1])

    # read in the winning numbers
    winning_numbers = " ".join(s.split(':')[1].split('|')[0].split()).split(' ')
    card['winning_numbers'] = [int(i) for i in winning_numbers]
    
    # read in the card numbers
    numbers = " ".join(s.split('|')[1].split()).split(' ')
    card['numbers'] = [int(i) for i in numbers]

    return card

def eval_card(c):
    matches = list(set(card['numbers']) & set(card['winning_numbers']))
    print(matches)

    if len(matches) == 0:
        return 0
    else:
        return 2 ** (len(matches) - 1)

if __name__ == '__main__':
    total = 0

    with open('input.txt') as f:
        for line in f:
            card = read_card(line)
            total += eval_card(card)

    print(total)
