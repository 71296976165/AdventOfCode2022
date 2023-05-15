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

outside_trees = len(map) - 1 + len(map) - 1 + len(map[0]) - 1 + len (map[0]) - 1
inside_trees = 0

for i, line in enumerate(map):
    visibility.append([])
    for j, tree in enumerate(line):
        visible = False
        if i != 0 and j != 0 and i != len(map)-1 and j != len(map)-1:
            LineofSight = True
            for k in range(len(map[0])):
                if k == j:
                    if LineofSight == True:
                        visible = True
                    #print("At map location: " + str(i) + ", " + str(j) + ". the west-facing Line of Sight is: " + str(LineofSight))
                    LineofSight = True
                else:
                    if map[i][k] >= tree:
                        LineofSight = False
            if LineofSight == True:
                visible = True
            #print("At map location: " + str(i) + ", " + str(j) + ". the east-facing Line of Sight is: " + str(LineofSight))
            LineofSight = True
            for k in range(len(map)):
                if k == i:
                    if LineofSight == True:
                        visible = True
                    #print("At map location: " + str(i) + ", " + str(j) + ". the north-facing Line of Sight is: " + str(LineofSight))
                    LineofSight = True
                else:
                    if map[k][j] >= tree:
                        LineofSight = False
            if LineofSight == True:
                visible = True
            #print("At map location: " + str(i) + ", " + str(j) + ". the south-facing Line of Sight is: " + str(LineofSight))
            if visible == True:
                inside_trees += 1
        visibility[i].append(visible)

# for line in visibility:
#     print(line)

print("The number of trees visible from outside the grid is: " + str(outside_trees + inside_trees))

f.close()