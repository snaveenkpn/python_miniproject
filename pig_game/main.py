import random

def roll():
    min_value=1
    max_value=6

    dice=random.randint(min_value,max_value)
    

    return dice



while True:
    players=input("Please enter the number of players: ")

    if players.isdigit():
        players_count = int(players)
        if 2 <= players_count <= 4:
            break
        else:
            print("please enter a number between 1 to 4")
    else:
        print("please enter a valid digit")


players_scores = [0 for _ in range(players_count)]

max_score=30

while max(players_scores) < max_score:

    for player_idx in range(players_count):
 
        current_score=0
        print (f"player {player_idx + 1} is started the game and score is {current_score}")

        while True:
            game_status=input("Do you want to start/continue the game (y): ")
            if game_status.lower() != "y":
                break
            else:
                value = roll()

            if value == 1:
                print("Your dice value is 1, you lose your chance")
                break

            print(f"The dice value is {value}")
            current_score += value

        players_scores[player_idx]=current_score

        print(f"The total score of player {player_idx + 1} is {players_scores[player_idx]}")

player_max= max(players_scores)

winner= players_scores.index(player_max)


print(f"The winner is player {winner}")


        
    





