print("Enter a source file:")
loc = input()
f = open(loc, "r")

file = []

for line in f:
    line = line.strip('\n')
    file.append(line)

matrix = []

linelength = len(file[0]) + 1
matrixwidth = linelength//4
for i in range(matrixwidth):
    matrix.append([])

instructionStart = 0

for i, line in enumerate(file):
    if line[1] == '1':
        instructionStart = i + 2
        break
    for i in range(matrixwidth):
        element = line[4*i + 1]
        if element != ' ':
            matrix[i].append(element)

for i in range(len(matrix)):
    matrix[i].reverse()
# now I have a list of lists which represents our crate stacking. 
# This arrangement allows us O(1) time rearrangement, which is important on the input file

for line in file[instructionStart:]:
    commands = line.split(" ")
    moves = int(commands[1])
    start = int(commands[3]) - 1
    end = int(commands[5]) - 1
    for i in range(moves):
        element = matrix[start].pop()
        matrix[end].append(element)

# this will create the final string for me
finalstring = ""
for list in matrix:
    finalstring += list.pop()

print(finalstring)

f.close()