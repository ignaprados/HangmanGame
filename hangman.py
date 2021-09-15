# import the random python module to pick a random word fro the hangman guessing words:
import random
from hangman_guessing import guess_list

guessing_word = random.choice(guess_list).lower()
word_letters = len(guessing_word)

game_over = False
tries = 6

#Import the game name from hangman_life.py and print it at the game start:
from hangman_life import game_name
print(game_name)

#Testing your code:
print(f'The word you guessed is {guessing_word}.')

#Create blank list called result to add right letters that the players have guessed to it:
result = []
for _ in range(word_letters):
    result += "_"
# iterate over the players input letters if the game not yet end:
while not game_over:
    user_guessing = input("Guess a letter: ")

    # If the players enter a letter that they guessed, print the letter and let them know:
    if user_guessing in result:
        print(f"The letter you guess {user_guessing}")

    #Now check if the guessed letter is right or wrong
    for position in range(word_letters):
        letter = guessing_word[position]
        #print the current oposition of the right letter that the players have guessed:
        if letter == user_guessing:
            result[position] = letter

    #Check if the players guess the wrong letter they will lose a try.
    if user_guessing not in guessing_word:
        #If the letter is not in the guessed_word, print out the letter and let them know it's not in the word.
        print(f"You guessed {user_guessing}, this letter is not in the word, You lose a try.")
        # after the players lose all of their tries they will lose the game and  
        tries -= 1
        if tries == 0:
            game_over = True
            print("You are a loser, Game Over.")

    #Join all the elements in the result list and turn it into a String.
    print(f"{' '.join(result)}")

    #Check if the players has got all the right letters so they will win the game.
    if "_" not in result:
        game_over = True
        print("You are a winner, Congratulations.")

    # Import the lives from hangman_life.py module and make this error go away.
    from hangman_life import lives
    print(lives[tries])