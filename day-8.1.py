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

# The length works fine to obtain the len(map)

outside_trees = 4 * (len(map)-1)
inside_trees = 0

# for i, line in enumerate(map):
#     visibility.append([])
#     for j, tree in enumerate(line):
#         visibility[i].append([])
#         # west check first
#         if j == 0:
#             visibility[i][j].append(0)
#         else:
#             westtree = map[i][j-1]
#             if visibility[i][j-1][0] > westtree:
#                 westtree = visibility[i][j-1][0]
#             visibility[i][j].append(westtree)
#         # north check
#         if i == 0:
#             visibility[i][j].append(0)
#         else:
#             northtree = map[i-1][j]
#             if visibility[i][j-1][1] > northtree:
#                 westtree = visibility[i][j-1][0]
#             visibility[i][j].append(northtree)
#         # east check
#         if j == len(map):
#             visibility[i][j].append(0)
#         else:
#             easttree = map[i][j+1]
#             visibility[i][j].append(easttree)
#         # south check
#         if i == len(map):
#             visibility[i][j].append(0)
#         else:
#             southtree = map[i+1][j]
#             visibility[i][j].append(southtree)

for i, line in enumerate(map):
    visibility.append([])
    for j, tree in enumerate(line):
        currTree = tree
        visible = False
        if i != 0 and j != 0 and i != len(map)-1 and j != len(map)-1:
            # check west
            LineofSight = True
            for k in range(j):
                if map[i][k] >= tree:
                    LineofSight = False
            if LineofSight == True:
                visible = True
            # check north
            LineofSight = True
            for k in range(i):
                if map[k][j] >= tree:
                    LineofSight = False
            if LineofSight == True:
                visible = True
            # check east
            LineofSight = True
            for k in range(len(map)-j):
                if map[i][len(map)-k-1] >= tree:
                    LineofSight = False
            if LineofSight == True:
                visible = True
            # check south
            LineofSight = True
            for k in range(len(map)-i):
                if map[len(map)-k-1][j] >= tree:
                    LineofSight = False
            if LineofSight == True:
                visible = True
            if visible == True:
                inside_trees += 1
        visibility[i].append(visible)

for line in visibility:
    print(line)

print("The number of trees visible from outside the grid is: " + str(outside_trees + inside_trees))

f.close()