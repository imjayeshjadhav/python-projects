import random
import time

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll

players = 2 # User and AI

# Game ends when any player reaches this score, a winning condition
max_score = 30

player_scores = [0 for _ in range(players)]
# List to store scores of both players, Index 0= User, Index 1 = AI
# List comprehension user for concise initialization - useful in many contexts (e.g initializing matrices, zero-padding)

# Game loop continues until one of the player reaches the winning score
while max(player_scores) < max_score:
    # max(player_scores) returns the highest score in the list - loop continues until it's >= max_score

    # Loop through each player one by one
    for player_idx in range(players):
        if player_idx == 0:
            print("\nYour turn has just started\n")
        else:
            print("\nAI's turn has just started\n")

        current_score = 0
        # current turn score for the player - resets each turn

        while True: # This inner loop continues until the player decides to stop rolling or rolls a 1
            if player_idx == 0:
                # User's turn: ask whether they want to roll
                should_roll = input("Would you like to roll (y)? ")

                if should_roll.lower() != "y":
                    break
            else :
                # AIs's logic for whether to roll or not
                if current_score < 10:
                    # Simple strategy: if AI has less than 10 in current turn, it will roll again
                    should_roll ="y"
                    print("AI Decides to roll.")
                    time.sleep(1)
                else :
                    print("AI decides to hold.")
                    time.sleep(1)
                    break
        
            value = roll() # Roll the die and store the result in value
            time.sleep(1)

            if value == 1:
                # Rolling 1 means you loose all points from this turn
                print("Rolled a 1! Turn over, no points this round.")
                current_score=0
                break
            else:
                current_score+=value
                print("Rolled: ", value)
                print("Current turn score:", current_score)

                if player_scores[player_idx] + current_score >= max_score:
                    player_scores[player_idx] += current_score
                    if player_idx == 0 :
                        print(f"\n🎉 You won the game with {player_scores[0]} points!")
                    else:
                        print(f"\n🤖 AI wins with {player_scores[1]} points! Better luck next time.\n")
                    exit()
        
        # After the inner turn ends, add the current turn score to that player's total
        player_scores[player_idx] += current_score
        if player_idx ==0:
            print("Your total score is:", player_scores[player_idx])
        else:
            print("AI total score is:", player_scores[player_idx])

        # Check after each turn if someone has won
        if player_scores[player_idx] >= max_score:
            break

    if max(player_scores) >= max_score:
        break # break out of while loop

# After the game loop ends, determine who won
if player_scores[0] >= max_score:
    print(f"\n🎉 You won the game with {player_scores[0]} points!")
else:
    print(f"\n🤖 AI wins with {player_scores[1]} points! Better luck next time.")
 
