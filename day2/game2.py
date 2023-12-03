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

def eval_game(game):
    # find the minimum number of each color that could've been used to play the game and return the power value
    # for the game (num_red * num_green * num_blue)
    num_red = 0
    num_green = 0
    num_blue = 0

    for round in game['rounds']:
        if 'red' in round and round['red'] > num_red:
            num_red = round['red']
        if 'green' in round and round['green'] > num_green:
            num_green = round['green']
        if 'blue' in round and round['blue'] > num_blue:
            num_blue = round['blue']

    return num_red * num_green * num_blue

if __name__ == "__main__":
    total = 0

    with open('input.txt') as f:
        for line in f:
            game = load_game(line)
            print(game)
            total += eval_game(game)

    print(total)
