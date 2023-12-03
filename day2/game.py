#!/usr/bin/env python3

def load_game(s):
    game = {}

    # extract the game id from the passed in string
    game['id'] = int(s.split(':')[0].split(' ')[1])

    # extract out the rounds
    rounds = s.split(':')[1].split(';')

    # extract out the number of each color out of each round
    game['rounds'] = []
    for round in rounds:
        round = round.strip().split(',')
        round_dict = {}
        round_total = 0
        for c in round:
            c = c.strip().split(' ')
            round_dict[c[1]] = int(c[0])
            round_total += int(c[0])
        round_dict['total'] = round_total
        game['rounds'].append(round_dict)
        
    return game

def eval_game(game, num_red, num_green, num_blue):
    # evaluate each round in the game to see if the number of each color is possible, along with the total
    num_total = num_red + num_green + num_blue

    for round in game['rounds']:
        if 'red' in round and round['red'] > num_red:
            return False
        if 'green' in round and round['green'] > num_green:
            return False
        if 'blue' in round and round['blue'] > num_blue:
            return False
        if round['total'] > num_total:
            return False

    return True

if __name__ == "__main__":
    total = 0

    with open('input.txt') as f:
        for line in f:
            game = load_game(line)
            print(game)
            if eval_game(game, 12, 13, 14):
                total += game['id']

    print(total)
