#!/usr/bin/env python3

import sys
sys.path.append('../common')

import util

def calc_next_in_sequence(l: list) -> int:
    if len(l) == 0:
        return 0
    if all(v == 0 for v in l):
        return 0

    # make a new list of differences
    n = []
    for i in range(len(l) - 1):
        n.append(l[i + 1] - l[i])
    return l[-1] + calc_next_in_sequence(n)

if __name__ == '__main__':
    total = 0

    with open('input.txt') as f:
        for l in f:
            seq = util.int_list_from_string(l)
            n = calc_next_in_sequence(seq)
            total += n

    print(f'total = {total}')
