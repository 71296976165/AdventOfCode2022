#First, let's get our input files. Our file will take input as loc,
#and we will then open the file at that file name with read input.
#Since I'm the one using this code, I will not have error-handling.

print("Enter a source file:")
loc = input()
f = open(loc, "r")

sumPriority = 0

for line in f:
    linelength = len(line)
    front = line[0:linelength//2]
    back = line[linelength//2:]
    ele = ''
    for frontele in front:
        for backele in back:
            if frontele == backele:
                ele = backele
    charValue = ord(ele) - ord('a')
    if charValue < 0:
        charValue = ord(ele) - ord('A')
        charValue += 26
    charValue += 1
    sumPriority += charValue

print(sumPriority)

f.close()