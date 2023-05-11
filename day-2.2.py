#First, let's get our input files. Our file will take input as loc,
#and we will then open the file at that file name with read input.
#Since I'm the one using this code, I will not have error-handling.

print("Enter a source file:")
loc = input()
f = open(loc, "r")

#This is a game of rock-paper-scissors.
# A = Rock, B = Paper, C = Scissors
# In this case
# X = Lose, Y = Draw, Z = Win
# Rock = 1, Paper = 2, Scissors = 3

#In this situation, it actually makes sense to consider whether to win or not first.
playerWins = 0
for line in f:
    #I'm assuming that f is well-formatted (I literally control the input file)
    plays = []
    plays.append(line[0])
    plays.append(line[2])
    if plays[1] == 'X':
        playerWins += 0
        if plays[0] == 'A':
            playerWins += 3
        elif plays[0] == 'B':
            playerWins += 1
        elif plays[0] == 'C':
            playerWins += 2
    elif plays[1] == 'Y':
        playerWins += 3
        if plays[0] == 'A':
            playerWins += 1
        elif plays[0] == 'B':
            playerWins += 2
        elif plays[0] == 'C':
            playerWins += 3
    elif plays[1] == 'Z':
        playerWins += 6
        if plays[0] == 'A':
            playerWins += 2
        elif plays[0] == 'B':
            playerWins += 3
        elif plays[0] == 'C':
            playerWins += 1

print(playerWins)

#clean up after ourselves
f.close()