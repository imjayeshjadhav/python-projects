import random 
import string
from words import words

# print(words)

# function to get valid word from the list
def get_valid_word(words):
    word = random.choice(words) # randomly choose something from list
    while '-' in word or ' ' in word: # keep choosing word if it is contains - or " "
        word = random.choice(words)
    return word # return a valid word

def hangman():
    word = get_valid_word(words).upper() # get a valid word and convert it to uppercase

    word_letters = set(word) #letters in the word
    # create a set of unique letters in the word (used to track what's left to guess)

    alphabet = set(string.ascii_uppercase)
    # create a set of all uppercase english letters (used to validate user input)

    used_letters = set() # what the user has gussed
    # create an empty set to keep track of letters that user has guessed

    lives = 6

    # Pre-fill 20% of the word with random correct guessed

    # Calculate how many letters to reveal 
    # use at least 1 letter even after the word is very short 
    num_to_reveal = max(1,len(word)//5)

    # Randomly select num_to_reveal unique letters from the word(word_letters set)
    pre_filled_letters = random.sample(list(word_letters), num_to_reveal)

    # Add these selected letters to the set of guessed letters (they will be visible)
    used_letters.update(pre_filled_letters)

    # Remove these revealed letters from word_letters (so user does't need to guess) 
    word_letters.difference_update(pre_filled_letters)

    # getting user input
    while len(word_letters) > 0 and lives > 0 :
        # display the letters that has already gussed
        print("\nYou have ",lives," lives left and You have used these letters: ",' '.join(used_letters))

        # create a list showing the current guessed word with dashes for unguessed letters
        word_list = [letter if letter in used_letters else '-' for letter in word]
        
        print('Current Word: ',' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
    
        # If the input is valid, new letter (not gussed before)
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter) # add to guessed letter
            if user_letter in word_letters:
                # correct guess: remove it from the set of remaining letters 
                word_letters.remove(user_letter)
            else:
                lives = lives-1
                print('Letter is not in the word')

        # If the letter was already gussed 
        elif user_letter in used_letters:
            print('You have already gussed that word.Please try again')
        
        # If the input is not a valid letter
        else:
            print("Invalid charater. Please try again")

    # gets here when len(word_letters) == 0
    if lives ==0:
        print("\nYou Died, The word was ", word, " 🤣")
    else:
        print(f"\nYay! You guessed the word: {word} correctly 💯🏆")

hangman()