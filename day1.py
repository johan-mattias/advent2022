from sys import stdin
#part 2
sums = [0]
index = 0
for line in stdin:
    if line == "\n":
        index += 1
        sums.append(0)
    else:
        sums[index] += int(line)
sums = sorted(sums)[::-1]
print(sums)
sum = sums[0]+sums[1]+sums[2]
print(sum)


# part 1
'''
max = 0
sum = 0
for line in stdin:
    print(line)
    if line == "\n":
        if sum > max:
           max = sum
        sum = 0
    else:
        sum += int(line)
print(max)
'''
         