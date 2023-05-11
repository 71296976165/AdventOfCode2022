#First, let's get our input files. Our file will take input as loc,
#and we will then open the file at that file name with read input.
#Since I'm the one using this code, I will not have error-handling.

print("Enter a source file:")
loc = input()
f = open(loc, "r")

totalOverlaps = 0

for line in f:
    line = line.strip('\n')
    sections = line.split(',')
    rows = []
    for section in sections:
        rows.append(section.split('-'))
    firststart = int(rows[0][0])
    firstend = int(rows[0][1])
    secondstart = int(rows[1][0])
    secondend = int(rows[1][1])

    if firststart < secondstart:
        #in this situation, the first starting index is less than the second starting index
        #therefore, the first elf's responsibilities encompass the second elf's if the ending index of the second elf is less than or equal to the first elf's ending index
        if firstend >= secondend:
            totalOverlaps += 1
    elif firststart > secondstart:
        if firstend <= secondend:
            totalOverlaps += 1
    else:
        totalOverlaps += 1
    #print(firststart,firstend,secondstart,secondend)

print(totalOverlaps)

f.close()