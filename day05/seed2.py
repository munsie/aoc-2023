#!/usr/bin/env python3

import sys
sys.path.append('../common')

import progress
import util

def read_range_map(f):
    # read the header line
    f.readline()

    m = []
    while True:
        s = util.trim(f.readline())
        if s == '':
            break
        m.append(util.int_list_from_string(s))

    return m

def find_in_range_map(m, v):
    for r in m:
        if v >= r[1] and v < (r[1] + r[2]):
            return r[0] + v - r[1]
    return v

if __name__ == '__main__':
    seeds = None
    seed_to_soil_map = None
    soil_to_fertilizer_map = None
    fertilizer_to_water_map = None
    water_to_light_map = None
    light_to_temperature_map = None 
    temperature_to_humidity_map = None
    humidity_to_location_map = None

    # load all of our input data
    with open('input.txt') as f:
        # read the list of seeds first
        it = iter(util.int_list_from_string(util.trim(f.readline().split(':')[1])))
        seeds = list(zip(it, it))
        
        f.readline()

        # load in the range maps
        seed_to_soil_map = read_range_map(f)
        soil_to_fertilizer_map = read_range_map(f)
        fertilizer_to_water_map = read_range_map(f)
        water_to_light_map = read_range_map(f)
        light_to_temperature_map = read_range_map(f)
        temperature_to_humidity_map = read_range_map(f)
        humidity_to_location_map = read_range_map(f)

    # for each seed, we need to find the location
    lowest_seed = 0
    lowest_location = 99999999999999999999

    # calculate how many seeds we're going to lookup
    num_items = 0
    for seed_range in seeds:
        num_items += seed_range[1]

    cur_item = 1
    for seed_range in seeds:
        for seed in range(seed_range[0], seed_range[0] + seed_range[1]):
            if not (cur_item % 1000):
                progress.update_items(cur_item, num_items, bar_width = 80, bar_type = progress.ANIMATED_RAINBOW)
            
            cur_item += 1

            soil = find_in_range_map(seed_to_soil_map, seed)
            fertilizer = find_in_range_map(soil_to_fertilizer_map, soil)
            water = find_in_range_map(fertilizer_to_water_map, fertilizer)
            light = find_in_range_map(water_to_light_map, water)
            temperature = find_in_range_map(light_to_temperature_map, light)
            humidity = find_in_range_map(temperature_to_humidity_map, temperature)
            location = find_in_range_map(humidity_to_location_map, humidity)

            #print(f'Seed {seed}, soil {soil}, fertilizer {fertilizer}, water {water}, light {light}, temperature {temperature}, humidity {humidity}, location {location}')
            
            if location < lowest_location:
                lowest_location = location
                lowest_seed = seed

    progress.update_items(cur_item, num_items, bar_width = 80, suffix = ' Done!')
    print(f'\n\nlowest_location = {lowest_location}, seed = {lowest_seed}')
