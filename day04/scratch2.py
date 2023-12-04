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
    return len(matches)

if __name__ == '__main__':
    card_mult = {}

    with open('input.txt') as f:
        for line in f:
            card = read_card(line)
            cid = card['id']
            
            card_mult.setdefault(cid, 0)
            card_mult[cid] += 1

            value = eval_card(card)

            for i in range(0, value):
                card_mult.setdefault(cid + 1 + i, 0)
                card_mult[cid + 1 + i] += card_mult[cid]

    print(sum(card_mult.values()))
