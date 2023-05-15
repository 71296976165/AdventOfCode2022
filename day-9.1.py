print("Enter a source file:")
loc = input()
f = open(loc, "r")

tailPath = {}
count = 0
headX = 0
headY = 0
tailX = 0
tailY = 0

for line in f:
    #
    line = line.strip('\n')
    directions = line.split()

    for i in range(int(directions[1])):
        if directions[0] == 'R':
            headX += 1
        elif directions[0] == 'L':
            headX += -1
        elif directions[0] == 'U':
            headY += 1
        elif directions[0] == 'D':
            headY -= 1
        #head move complete, let's look at the tail moving
        if abs(headX - tailX) > 1:
            if directions[0] == 'R':
                tailX += 1
            elif directions[0] == 'L':
                tailX += -1
            if headY - tailY == 1:
                tailY += 1
            elif headY - tailY == -1:
                tailY += -1
        if abs(headY - tailY) > 1:
            if directions[0] == 'U':
                tailY += 1
            elif directions[0] == 'D':
                tailY += -1
            if headX - tailX == 1:
                tailX += 1
            elif headX - tailX == -1:
                tailX += -1
        #
        tailLocation = (tailX, tailY)
        tailPath[tailLocation] = 'v'

print(len(tailPath.keys()))

f.close()