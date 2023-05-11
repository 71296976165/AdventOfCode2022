#First, let's get our input files. Our file will take input as loc,
#and we will then open the file at that file name with read input.
#Since I'm the one using this code, I will not have error-handling.

print("Enter a source file:")
loc = input()
f = open(loc, "r")

sumPriority = 0

#In the second part of day 3, we actually need multiple sections - therefore I'll just use more data for this

groups = []

for line in f:
    groups.append(line)

for i in range(len(groups)//3):
    first = groups[3*i]
    second = groups[3*i+1]
    third = groups[3*i+2]
    first = first.strip('\n')
    second = second.strip('\n')
    third = third.strip('\n')
    ele = ''
    for firstele in first:
        for secondele in second:
            if firstele == secondele:
                for thirdele in third:
                    if thirdele == secondele:
                        ele = thirdele
    charValue = ord(ele) - ord('a')
    if charValue < 0:
        charValue = ord(ele) - ord('A')
        charValue += 26
    charValue += 1
    sumPriority += charValue

print(sumPriority)

f.close()