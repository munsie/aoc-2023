#!/usr/bin/env python3

total = 0

DIGITS = [ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' ]
NUMBERS = [ 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine' ]

def find_lowest_index_in_list(s, l):
    offset = len(s)
    value = -1
    for i in range(0, len(l)):
        o = s.find(l[i])
        if o != -1 and o < offset:
            offset = o
            value = i

    return value, offset

def rfind_highest_index_in_list(s, l):
    offset = -1
    value = -1
    for i in range(0, len(l)):
        o = s.rfind(l[i])
        if o != -1 and o > offset:
            offset = o
            value = i

    return value, offset

def find_number(s):
    # look for digits first
    digits_value, digits_offset = find_lowest_index_in_list(s, DIGITS)

    # look for spelled out numbers next
    numbers_value, numbers_offset = find_lowest_index_in_list(s, NUMBERS)

    # return the one that was closer to the start of the string
    if digits_offset < numbers_offset:
        return digits_value
    else:
        return numbers_value

def rfind_number(s):
    # look for digits first
    digits_value, digits_offset = rfind_highest_index_in_list(s, DIGITS)

    # look for spelled out numbers next
    numbers_value, numbers_offset = rfind_highest_index_in_list(s, NUMBERS)

    # return the one that was closer to the end of the string
    if digits_offset > numbers_offset:
        return digits_value
    else:
        return numbers_value

with open('input.txt') as f:
    for line in f:
        first_digit = find_number(line)
        last_digit = rfind_number(line)
        line_value = int(str(first_digit) + str(last_digit))
        total = total + int(line_value)

print(total)
