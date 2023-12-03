#!/usr/bin/env python3

total = 0

with open('input2.txt') as f:
    for line in f:
        first_digit = line[[x.isdigit() for x in line].index(True)]
       
        rev_line = "".join(reversed(line))
        last_digit = rev_line[[x.isdigit() for x in rev_line].index(True)]

        line_value = first_digit + last_digit
        total = total + int(line_value)

print(total)
