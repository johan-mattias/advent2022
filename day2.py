#day2.py
from sys import stdin
score = 0

for line in stdin:
    move, result = line.split()
    
    print(move, result)
    if move == 'A':
        if result == 'X':
            #tie
            score += (3+1)
        elif my_move == 'Y':
            #win
            score += (6+2)
        elif my_move == 'Z':
            #lose
            score += (0+3)
        else:
            print('fail my_move', my_move)
    elif move == 'B':
        if my_move == 'X':
            #lose
            score += (0+1)
        elif my_move == 'Y':
            #tie
            score+= (3+2)
        elif my_move == 'Z':
            #win
            score+=(6+3)
        else:
            print('fail my_move', my_move)

    elif move == "C":
        if my_move == 'X':
            #win
            score+=(6+1)
        elif my_move == 'Y':
            #lose
            score+=(0+2)
        elif my_move == 'Z':
            #tie
            score+=(3+3)
        else:
            print('fail my_move', my_move)

    else:
        print('fail move: ', move)
    print(score)
print(score)

#part 1
'''
score = 0

for line in stdin:
    move, my_move = line.split()
    
    print(move, my_move)
    if move == 'A':
        if my_move == 'X':
            #tie
            score += (3+1)
        elif my_move == 'Y':
            #win
            score += (6+2)
        elif my_move == 'Z':
            #lose
            score += (0+3)
        else:
            print('fail my_move', my_move)
    elif move == 'B':
        if my_move == 'X':
            #lose
            score += (0+1)
        elif my_move == 'Y':
            #tie
            score+= (3+2)
        elif my_move == 'Z':
            #win
            score+=(6+3)
        else:
            print('fail my_move', my_move)

    elif move == "C":
        if my_move == 'X':
            #win
            score+=(6+1)
        elif my_move == 'Y':
            #lose
            score+=(0+2)
        elif my_move == 'Z':
            #tie
            score+=(3+3)
        else:
            print('fail my_move', my_move)

    else:
        print('fail move: ', move)
    print(score)
print(score)
'''