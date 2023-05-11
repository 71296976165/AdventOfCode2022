#First, let's get our input files. Our file will take input as loc,
#and we will then open the file at that file name with read input.
#Since I'm the one using this code, I will not have error-handling.

print("Enter a source file:")
loc = input()
f = open(loc, "r")

#This is a game of rock-paper-scissors.
# A = Rock, B = Paper, C = Scissors
# X = Rock, Y = Paper, Z = Scissors

#There's no particular reason to be risky with this. We'll use direct comparisons.
playerWins = 0
for line in f:
    plays = []
    plays.append(line[0])
    plays.append(line[2])
    if plays[0] == 'A':
        if plays[1] == 'X':
            playerWins += 1
            playerWins += 3
        elif plays[1] == 'Y':
            playerWins += 2
            playerWins += 6
        elif plays[1] == 'Z':
            playerWins += 3
            playerWins += 0
    elif plays[0] == 'B':
        if plays[1] == 'X':
            playerWins += 1
            playerWins += 0
        elif plays[1] == 'Y':
            playerWins += 2
            playerWins += 3
        elif plays[1] == 'Z':
            playerWins += 3
            playerWins += 6
    elif plays[0] == 'C':
        if plays[1] == 'X':
            playerWins += 1
            playerWins += 6
        elif plays[1] == 'Y':
            playerWins += 2
            playerWins += 0
        elif plays[1] == 'Z':
            playerWins += 3
            playerWins += 3

print(playerWins)

#clean up after ourselves
f.close()