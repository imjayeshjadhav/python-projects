import random
import time

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll

max_score = 50 

# Ask user how many players will participate in the game
while True:
    try:
        players = int(input("How many players are there in the game (2-4)? "))
        if 2 <= players <= 4:
            break
        else:
            print("Please enter a number between (2-4)? ")
    except ValueError:
        print("Invalid input! please enter a number!!")

# Initialize all player scores to 0 using list comprehension
# player_scores[0] = Player 1, player_scores[1] = Player 2
player_scores = [0 for _ in range(players)]

# Game loop continues until someone reaches the max_score

while max(player_scores) < max_score:
    # Loop over each player one by one for their turn
    for player_idx in range(players):
        print(f"\nPlayer {player_idx+1}'s turn has just started\n")

        current_score = 0 # temporary score for this turn only

        while True: # Inner loop continues until player holds or rolls a 1
            should_roll  = input(f"Player {player_idx+1}, would you like to roll? (y/n): ").lower()

            if should_roll != "y":
                print("You choose to hold. Ending turn.")
                break # End turn if player chooses not to roll

            value = roll() # simulate rolling the dice
            time.sleep(1) 
            print(f"🎯 Rolled: {value}")

            if value == 1:
                # Rolling 1 ends the turn and scores 0 for the round
                print("❌ Oops! Rolled a 1. You get no points this round")
                current_score=0
                break # return immediately
            else:
                current_score += value
                print(f"📈 Current turn score: {current_score}")

                # check if this roll results in a win
                if player_scores[player_idx] + current_score >= max_score:
                    player_scores[player_idx] += current_score # Adds points to total
                    print(f"\n🏁 Game Over! Player {player_idx+1} wins with {player_scores[player_idx]} points! 🎉")
                    exit() # End the game completely
        
        # Add the points scored in this round to the player's total
        player_scores[player_idx] += current_score
        print(f" Player {player_idx+1}'s total score is now: {player_scores[player_idx]}")

# Final check after the main loop ends
# This part won't usually execute beacause we exit early when someone wins
winner_index = player_scores.index(max(player_scores))
print(f"\n🏁 Game Over! Player {winner_index + 1} wins with {player_scores[winner_index]} points! 🎊")



        



