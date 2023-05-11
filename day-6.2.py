print("Enter a source file:")
loc = input()
f = open(loc, "r")

line = f.readline()

# I need a datastructure with a limited size, that can push in from the back and pop out the front.
# Like I thought, I need size 13 (for 14 letter long packets) this time.
# This sounds like a deque.

from collections import deque

marker = deque()

for i in range(13):
    marker.append(line[i])

print(marker)

for i, letter in enumerate(line[13:]):
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
        print(i+14)
        break
    else:
        marker.popleft()
print(marker)

f.close()