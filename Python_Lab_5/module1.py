from random import randint
import time

def input_name(num):
    print("Name of player ".format(num))
    return input()
def throws(namePlayer):
    print("Dice rolls ", namePlayer)
    time.sleep(2)
    points = randint(1, 6)
    print("Result: ", points)
    return points
def game_dice(namePlayer1, namePlayer2):
    numOfThrows = int(input("Number of throws "))
    summPointsPlayer1 = 0
    summPointsPlayer2 = 0
    for i in range(numOfThrows):
        print("Step ", i + 1)
        summPointsPlayer1 += throws(namePlayer1)
        summPointsPlayer2 += throws(namePlayer2)
    print(namePlayer1, "point: ", summPointsPlayer1)
    print(namePlayer2, "point: ", summPointsPlayer2)
    return [summPointsPlayer1, summPointsPlayer2]

def winner(namePlayer1, namePlayer2, summPointsPlayer1, summPointsPlayer2):
    if summPointsPlayer1 > summPointsPlayer2:
        print("Win ", namePlayer1)
    elif summPointsPlayer1 < summPointsPlayer2:
        print("Win ", namePlayer2)
    else:
        print("Draw")