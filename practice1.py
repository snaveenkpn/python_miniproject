import random

MIN_VALUE=1
MAX_VALUE=6

players=input("please enter the number of players: ")


def roll():
    dice=random.randint(MIN_VALUE,MAX_VALUE)
    print(dice)


players_score=[0 for _ in range(int(players))]

print(players_score)
