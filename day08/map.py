#!/usr/bin/env python3

import sys
sys.path.append('../common')

import util

if __name__ == '__main__':
    with open('input.txt') as f:
        # read the directions
        directions = util.trim(f.readline())
        
        # read the blank line
        f.readline()

        # read the nodes
        nodes = {}
        for l in f:
            l = util.trim(l)

            # get the node name
            name = l.split()[0]
    
            # get the left and right nodes
            nodes[name] = l.split('(')[1].split(')')[0].replace(' ', '').split(',')

    # follow our directions to go from AAA to ZZZ
    current_node = 'AAA'
    steps = 0
    index = 0

    while current_node != 'ZZZ':
        dir = directions[index]
        index += 1
        if index == len(directions):
            index = 0

        current_node = nodes[current_node][0 if dir == 'L' else 1]
        steps += 1

    print(steps)
