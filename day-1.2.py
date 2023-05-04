print("Enter a source file:")
loc = input()
f = open(loc, "r")
tval = 0
elves =[]
carCal = 0
for cal in f:
    if cal == "\n":
        elves.append(carCal)
        carCal = 0
    else:
        xcal = int(cal)
        carCal += xcal
elves.append(carCal)
maxCal = [0,0,0]
for cal in elves:
    if cal > maxCal[0]:
        maxCal[0] = cal
        if cal > maxCal[1]:
            maxCal[0] = maxCal[1]
            maxCal[1] = cal
            if cal > maxCal[2]:
                maxCal[1] = maxCal[2]
                maxCal[2] = cal
for val in maxCal:
    print(val)
    tval += val
print(tval)
f.close()