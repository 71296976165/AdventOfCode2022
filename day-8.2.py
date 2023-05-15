print("Enter a source file:")
loc = input()
f = open(loc, "r")

map = []
visibility = []

for i, line in enumerate(f):
    map.append([])
    line = line.strip('\n')
    for letter in line:
        map[i].append(int(letter))

bestTree = [0,0,0]

for i, line in enumerate(map):
    visibility.append([])
    for j, tree in enumerate(line):
        scenery = []
        if i != 0 and j != 0 and i != len(map)-1 and j != len(map)-1:
            LineOfSight = True
            scenicLine = 0
            for k in range(j):
                if LineOfSight == True:
                    scenicLine += 1
                if map[i][j-k-1] >= tree:
                    LineOfSight = False
                    # print("At map location: " + str(i) + ", " + str(j) + ". the west-facing line of sight was broken at: " + str(i) + ", " + str(j-k-1))
            # print("At map location: " + str(i) + ", " + str(j) + ". the west-facing visible trees are: " + str(scenicLine))
            scenery.append(scenicLine)

            LineOfSight = True
            scenicLine = 0
            for k in range(len(map)-j):
                if k == 0:
                    continue
                if LineOfSight == True:
                    scenicLine += 1
                if map[i][j+k] >= tree:
                    LineOfSight = False
                    # print("At map location: " + str(i) + ", " + str(j) + ". the east-facing line of sight was broken at: " + str(i) + ", " + str(j+k))
            scenery.append(scenicLine)
            # print("At map location: " + str(i) + ", " + str(j) + ". the east-facing visible trees are: " + str(scenicLine))
            
            LineOfSight = True
            scenicLine = 0
            for k in range(i):
                if LineOfSight == True:
                    scenicLine += 1
                if map[i-k-1][j] >= tree:
                    LineOfSight = False
                    # print("At map location: " + str(i) + ", " + str(j) + ". the north-facing line of sight was broken at: " + str(i-k-1) + ", " + str(j))
            scenery.append(scenicLine)
            # print("At map location: " + str(i) + ", " + str(j) + ". the north-facing visible trees are: " + str(scenicLine))

            LineOfSight = True
            scenicLine = 0
            for k in range(len(map) - i):
                if k == 0:
                    continue
                if LineOfSight == True:
                    scenicLine += 1
                if map[i+k][j] >= tree:
                    LineOfSight = False
                    # print("At map location: " + str(i) + ", " + str(j) + ". the south-facing line of sight was broken at: " + str(i+k) + ", " + str(j))
            scenery.append(scenicLine)
            # print("At map location: " + str(i) + ", " + str(j) + ". the south-facing visible trees are: " + str(scenicLine))
            scenicScore = 1
            for x in scenery:
                scenicScore *= x
            visibility[i].append(scenicScore)
            if scenicScore > bestTree[2]:
                bestTree[0] = i
                bestTree[1] = j
                bestTree[2] = scenicScore
        else:
            visibility[i].append(0)

# for line in visibility:
#     print(line)

print("The best location for a treehouse is at: " + str(bestTree[0]) + ", " + str(bestTree[1]) + ". with a scenic score of: " + str(bestTree[2]))

f.close()