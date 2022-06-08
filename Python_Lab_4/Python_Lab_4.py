from random import randint
import time

#Name of players
igrok1 = input('First player name  ')
igrok2 = input('Second player name  ')
summ1 = 0
summ2 = 0

for i in range(5):
#First player game
    print('Rolls the dice', igrok1)
    time.sleep(2)
    n1 = randint(1, 6)
    print('Result:', n1)
    summ1 += n1
    

#Second player game
    print('Rolls the dice', igrok2)
    time.sleep(2)
    n2 = randint(1, 6)
    print('Result:', n2)
    summ2 += n2

#Result
if summ1 > summ2:
    print('Win  ', igrok1)
elif summ1 < summ2:
    print('Win  ', igrok2)
else:
    print('Draw')
