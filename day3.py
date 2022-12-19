from sys import stdin
from math import floor
from collections import defaultdict
from pprint import pprint


elves = []

badges = []

total = 0

for line in stdin:
    elves.append(line.rstrip())

for index in range(0,len(elves), 3):
    badge = set(elves[index]).intersection(
        set(elves[index+1]),  
        set(elves[index+2]))
    print(badge)
    badge = str(badge.pop())
    if badge.isupper():
        total += ord(badge)-38
    else:
        total += ord(badge)-96
print(total)

'''
for elf1 in elves:
    for elf2 in elves:
        if elf1 is not elf2:
            for letter in elf1:
                if letter in elf2:
                    print('hit', letter)
                    print('elf1', elf1)
                    print('elf2', elf2)
                    print()
                    badges[letter].add(elf1)
pprint(badges)

for badge, elves in badges.items():
    if len(elves) == 3:
        print(badge)
'''
'''
#part 1
sol = ''
sum = 0

for line in stdin:
    print(floor(len(line)/2))
    half = floor(len(line)/2)
    front, back = line[:half], line[half:]
    print(front,' yolo' ,back)
    for letter in front:
        if letter in back:
            sol += letter
            if letter.isupper():
                sum += ord(letter)-38
            else:
                sum += ord(letter)-96
            print(letter, ord(letter)-96 )
            break

print(sol)
print(sum)
            
'''