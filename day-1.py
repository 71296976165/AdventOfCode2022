print("Enter a source file:")
loc = input()
f = open(loc, "r")
maxCal = 0
carCal = 0
for cal in f:
    if cal == "\n":
        carCal = 0
    else:
        xcal = int(cal)
        carCal += xcal
        if carCal > maxCal:
            maxCal = carCal
print(maxCal)
f.close()