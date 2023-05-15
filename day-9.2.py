print("Enter a source file:")
loc = input()
f = open(loc, "r")

class Segment:
    def __init__(self, X, Y, ):
        self.x = X
        self.y = Y
    
    def move(self, other, direction):
        if abs(other.x - self.x) > 1:
            if other.x - self.x > 0:
                self.x += 1
            elif other.x - self.x > 0:
                self.x += -1
            if other.y - self.y == 1:
                self.y += 1
            elif other.y - self.y == -1:
                self.y += -1
        if abs(other.y - self.y) > 1:
            if other.y - self.y > 0:
                self.y += 1
            elif other.y - self.y < 0:
                self.y += -1
            if other.x - self.x == 1:
                self.x += 1
            elif other.x - self.x == -1:
                self.x += -1
    
    def movefirst(self, aheadX, aheadY, direction):
        if abs(aheadX - self.x) > 1:
            if aheadX - self.x > 0:
                self.x += 1
            elif aheadX - self.x < 0:
                self.x += -1
            if aheadY - self.y == 1:
                self.y += 1
            elif aheadY - self.y == -1:
                self.y += -1
        if abs(aheadY - self.y) > 1:
            if aheadY - self.y > 0:
                self.y += 1
            elif aheadY - self.y < 0:
                self.y += -1
            if aheadX - self.x == 1:
                self.x += 1
            elif aheadX - self.x == -1:
                self.x += -1
    
    def getCoords(self):
        return [self.x, self.y]

tailPath = {}
count = 0
headX = 0
headY = 0

for line in f:
    #
    line = line.strip('\n')
    directions = line.split()
    one = Segment(0,0)
    two = Segment(0,0)
    three = Segment(0,0)
    four = Segment(0,0)
    five = Segment(0,0)
    six = Segment(0,0)
    seven = Segment(0,0)
    eight = Segment(0,0)
    nine = Segment(0,0)
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
        one.movefirst(headX,headY, directions[0])
        two.move(one, directions[0])
        three.move(two,directions[0])
        four.move(three, directions[0])
        five.move(four, directions[0])
        six.move(five, directions[0])
        seven.move(six, directions[0])
        eight.move(seven, directions[0])
        nine.move(eight, directions[0])
        tailLoc = nine.getCoords()
        tailLocation = (tailLoc[0], tailLoc[1])
        tailPath[tailLocation] = 'v'

print(len(tailPath.keys()))
print(tailPath.keys())

f.close()