#!/usr/bin/env python3

def get_number_at(s, x, y):
    if y < 0 or y >= len(s):
        return 0, x, y

    row = s[y]
    if x < 0 or x >= len(row):
        return 0, x, y

    if not row[x].isdigit():
        return 0, x, y

    # find the bounds of the number
    start_x = x
    while True:
        if start_x == 0 or not row[start_x - 1].isdigit():
            break
        start_x -= 1

    end_x = x
    while True:
        if end_x == len(row) - 1 or not row[end_x + 1].isdigit():
            break
        end_x += 1

    return int(row[start_x:end_x + 1]), start_x, end_x

def get_part_number(s, x, y):
    # get the part number for the part located at x, y in the schematic.  This will be the sum of any number that
    # the part, even diagonally
   
    print(f'{x}, {y} = {s[y][x]}')

    # check the non-diagonals first
    check_ul = True
    check_ur = True
    check_bl = True
    check_br = True

    left, start, end = get_number_at(s, x - 1, y)
    if left != 0:
        print(f'  left = {left}')
    right, start, end = get_number_at(s, x + 1, y)
    if right != 0:
        print(f'  right = {right}')

    top, start, end = get_number_at(s, x, y - 1)
    if top != 0:
        print(f'  top = {top}')
        if start < x:
            check_ul = False
        if end > x:
            check_ur = False

    bottom, start, end = get_number_at(s, x, y + 1)
    if bottom != 0:
        print(f'  bottom = {bottom}')
        if start < x:
            check_bl = False
        if end > x:
            check_br = False

    print(f'  check_ul = {check_ul}, check_ur = {check_ur}, check_bl = {check_bl}, check_br = {check_br}')

    # now that we've checked the non-diagonals, we know which of the diagonals we should be checking
    ul = 0
    if check_ul:
        ul, start, end = get_number_at(s, x - 1, y - 1)
        if ul != 0:
            print(f'  ul = {ul}')
    ur = 0
    if check_ur:
        ur, start, end = get_number_at(s, x + 1, y - 1)
        if ur != 0:
            print(f'  ur = {ur}')
    bl = 0
    if check_bl:
        bl, start, end = get_number_at(s, x - 1, y + 1)
        if bl != 0:
            print(f'  bl = {bl}')
    br = 0
    if check_br:
        br, start, end = get_number_at(s, x + 1, y + 1)
        if br != 0:
            print(f'  br = {br}')

    part_number = left + right + top + bottom + ul + ur + bl + br
    print(f'  part_number = {part_number}')
    return part_number

def find_parts(s):
    # find the position of all of the parts in the schematic (i.e, any position not a digit or period)
    parts = []
    for y in range(0, len(s)):
        for x in range(0, len(s[y])):
            c = s[y][x]
            if not c.isdigit() and c != '.':
                number = get_part_number(s, x, y)
                parts.append([x, y, c, number])
    return parts

if __name__ == '__main__':
    # read in the schematic
    schematic = []
    with open('input.txt') as f:
        for line in f:
            schematic.append(line.rstrip())

    # find all of the parts
    parts = find_parts(schematic)

    total = 0
    for part in parts:
        print(f'{part}')
        total += part[3]

    print(f'total = {total}')

