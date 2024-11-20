#my answer for day 12 project --------------------------------------------------
# # import random
# game_end=False
# print("Welcome to the number Guessing Game!")
# print("I'm thinking of a number Between 1 and 100.")
# level=input("Choose a difficult. Type 'easy' and 'hard': ").lower()
# if level=="easy":
#     attempt=10
# elif level=="hard":
#     attempt=5
# else:
#     print("invalid level choose.")
# thinking_number=random.randint(1,100)
# print(thinking_number)
# def guess_number(make_guess_number,thinking_number,attempt):
#     global game_end
#     if make_guess_number==thinking_number:
#             print(f"You got it! The answer was {thinking_number}.")
#             game_end=True
#     elif make_guess_number>thinking_number:
#             print("Too high.\nGuess again.")
#     elif make_guess_number<thinking_number: 
#             print("Too low.\nGuess again.")  
    
#     if attempt==0 and game_end==False:
#             print("You've run out of guesses, you lose.")
#             game_end=True
#     return game_end

# while not game_end:
#         print(f"You have {attempt} attempts remaining to Guess the number.")
#         make_guess=int(input("Make a guess: "))
#         attempt-=1
#         guess_number(make_guess,thinking_number,attempt)




# -------------------------------------------------------------------------------------------------------------








#teacher answer for day 12 project -----------------------------------------------------------------
from random import randint
EASY_LEVEL_TURNS=10
HARD_LEVEL_TRUNS=5
#function to check user's guess actual answer.
def check_answer(guess,answer,turns):
        if guess>answer:
            print("Too high.")
            return turns - 1
        elif guess<answer:
            print("Too low.")
            return turns - 1
        elif guess==answer:
            print(f"You got it! The answer was {answer}.")
        else:
            print("invalid input.")
            return turns-1
#make function to set difficulty
def set_difficulty():
      level=input("Choose a difficulty. Type 'easy' or 'hard': ")
      if level == "easy":
            return EASY_LEVEL_TURNS
      elif level =="hard":
            return HARD_LEVEL_TRUNS
def game():
      #choosing a random number between 1 and 100
      print("Welcome to the number Guessing Game!")
      print("I'm thinking of a number Between 1 and 100.")
      answer=randint(1,100)
      turns=set_difficulty()
      #repeat the guessing functionality if they get it wrong.
      guess=0
      while guess!=answer:
            print(f"You have {turns} attempts remaining to Guess the number.")

            #let the user guess a number
            guess=int(input("Make a guess: "))
              
            #track the number of turnd and reduce by 1 if they get it wrong
            turns=check_answer(guess,answer,turns)
            if turns==0:
                 print("You've run out of guesses, you lose.")
                 return
            elif guess!=answer:
                 print("Guess again.")
                 
            
game()
             
