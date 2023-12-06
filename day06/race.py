#!/usr/bin/env python3

import sys
sys.path.append('../common')

import util

if __name__ == '__main__':
    with open('input.txt') as f:
        # read in the data
        times = util.int_list_from_string(util.trim(f.readline().split(':')[1]))
        distances = util.int_list_from_string(util.trim(f.readline().split(':')[1]))

    total = 1
    for i in range(0, len(times)):
        time = times[i]
        distance = distances[i]

        #print(f'Calculating options for race {i + 1}, time = {time}, distance = {distance}...')
        race_count = 0
        prev_distance = 0
        for j in range(0, time):
            new_distance = (time - (j + 1)) * (j + 1)
            #print(f'    {time - (j + 1)} * {j + 1} = {new_distance}') 
            if new_distance > distance:
                #print(f'  j = {j + 1} wins')
                race_count += 1
            elif new_distance < prev_distance:
                break

            prev_distance = new_distance

        total *= race_count

    print(total)
