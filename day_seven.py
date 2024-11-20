print("\n__________________________________________________________________\nDAY SEVEN\nHANGMAN GAME CHALLENGE \n__________________________________________________________________\n")
import os
def clear_console():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For macOS and Linux
    else:
        os.system('clear')
import random
 #Update the word list to use the 'word_list' from hangman_words.py
from hangman_words import word_list
#TODO-1 - step1:- Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word=random.choice(word_list)
word_length=len(chosen_word)
#  Create an empty List called display.
display=[]
#Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.
lives=6
from hangman_art import logo,stages
#Import the logo from hangman_art.py and print it at the start of the game.
print(logo)
#Testing code
print(f'Pssst, the solution is {chosen_word}.')
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
for letter in chosen_word:
    display.append("_")
print(f"{' '.join(display)}")

#TODO-2 -step1:- Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
#        step2:- Use a while loop to let the user guess again. 
# #The loop should only stop once the user has guessed all the letters in the chosen_word and 
#'display' has no more blanks ("_"). Then you can tell the user they've won.
end_of_game=False
while not end_of_game:
    guess=input("Guess a latter: ").lower()
    clear_console()
    #If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You've already guessed {guess}")
    #TODO-3 - step1:- Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

    #         step2: - Loop through each position in the chosen_word;
    #If the letter at that position matches 'guess' then reveal that letter in the display at that position.
    #e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
    # Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
    for letter in range (word_length):
        if chosen_word[letter]==guess:
            display[letter]=guess
     #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")
    #If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."
    if guess not in chosen_word:
        #If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives-=1
        if lives==0:
          end_of_game=True
          print("YOU LOSE!")
    #Check if user has got all letters.
    if "_" not in display:
        end_of_game=True
        print("YOU WIN")
   # Import the stages from hangman_art.py and make this error go away.
    print(stages[lives])
    if lives==0:
          print(f"THE CHOSEN WORD IS '{chosen_word}'")