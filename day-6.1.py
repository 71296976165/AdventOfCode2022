print("Enter a source file:")
loc = input()
f = open(loc, "r")

line = f.readline()

# I need a datastructure with a limited size, that can push in from the back and pop out the front.
# It'll only need to be three elements large at any given point for part 1 - however, I suspect part 2 will involve larger packet sizes.
# This sounds like a deque.

from collections import deque

marker = deque()

for i in range(3):
    marker.append(line[i])

print(marker)

for i, letter in enumerate(line[3:]):
    flag = True
    marker.append(letter)
    for test in marker:
        count = 0
        for other in marker:
            if test == other:
                count += 1
        if count > 1:
            flag = False
    if flag == True:
        print(i+4)
        break
    else:
        marker.popleft()
print(marker)

f.close()