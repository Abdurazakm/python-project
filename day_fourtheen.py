from os import system
system('cls')
import random
from higher_lower_game_art import logo, vs
from higher_lower_game_data import data


# def get_random_account():
#   """Get data from random account"""
#   return random.choice(data)

# def format_data(account):
#   """Format account into printable format: najme, description and country"""
#   name = account["name"]
#   description = account["description"]
#   country = account["country"]
#   # print(f'{name}: {account["follower_count"]}')
#   return f"{name}, a {description}, from {country}"

# def check_answer(guess, a_followers, b_followers):
#   """Checks followers against user's guess 
#   and returns True if they got it right.
#   Or False if they got it wrong.""" 
#   if a_followers > b_followers:
#     return guess == "a"
#   else:
#     return guess == "b"


# def game():
#   print(logo)
#   score = 0
#   game_should_continue = True
#   account_a = get_random_account()
#   account_b = get_random_account()

#   while game_should_continue:
#     account_a = account_b
#     account_b = get_random_account()

#     while account_a == account_b:
#       account_b = get_random_account()

#     print(f"Compare A: {format_data(account_a)}.")
#     print(vs)
#     print(f"Against B: {format_data(account_b)}.")
    
#     guess = input("Who has more followers? Type 'A' or 'B': ").lower()
#     a_follower_count = account_a["follower_count"]
#     b_follower_count = account_b["follower_count"]
#     is_correct = check_answer(guess, a_follower_count, b_follower_count)

#     system('cls')
#     print(logo)
#     if is_correct:
#       score += 1
#       print(f"You're right! Current score: {score}.")
#     else:
#       game_should_continue = False
#       print(f"Sorry, that's wrong. Final score: {score}")

# game()

# '''

# FAQ: Why does choice B always become choice A in every round, even when A had more followers? 

# Suppose you just started the game and you are comparing the followers of A - Instagram (364k) to B - Selena Gomez (174k). Instagram has more followers, so choice A is correct. However, the subsequent comparison should be between Selena Gomez (the new A) and someone else. The reason is that everything in our list has fewer followers than Instagram. If we were to keep Instagram as part of the comparison (as choice A) then Instagram would stay there for the rest of the game. This would be quite boring. By swapping choice B for A each round, we avoid a situation where the number of followers of choice A keeps going up over the course of the game. Hope that makes sense :-)

# '''



# Generate a random account from the game data.

# Format account data into printable format.

# Ask user for a guess.

# Check if user is correct.
# Get follower count.
# If Statement

# Feedback.

# Score Keeping.

# Make game repeatable.

# Make B become the next A.

# Add art.

# Clear screen between rounds.




# def comper():
#  pick_random=random.choice(data)
#  return pick_random








#Display art
print(logo)
score=0
account_b=random.choice(data)
game_should_countinue=True
# generate a random account form th game data
while game_should_countinue:
    account_a=account_b
    account_b=random.choice(data)
    if account_a==account_b:
        account_b=random.choice(data)
    # format the account data into printable format
    def format_account(account):
        account_name=account["name"]
        account_discrp=account["description"]
        account_country=account["country"]
        return f"{account_name}, a {account_discrp}, form {account_country}"
    def check_answer(guess,a_follower_count,b_follower_count):
        if a_follower_count>b_follower_count:
            return guess=="a"
        else:
            return guess=="b"
    print(f"comper A: {format_account(account_a)} ")
    print(vs)
    print(f"against b: {format_account(account_b)} ")
    # ask the user for a guess
    guess=input("Who has more followers? Type 'A' or 'B':").lower()
    #check if the user is correct
    a_follower_count=account_a["follower_count"]
    b_follower_count=account_b["follower_count"]
    is_correct=check_answer(guess, a_follower_count, b_follower_count)
    # clear the screan between round
    system('cls')
    print(logo)
    #give the user feedback on their guess.
    #score keeping
    if is_correct:
        score+=1
        print(f"You're right! Current score: {score}.")
    else:
        game_should_countinue=False
        print(f"Sorry, that's wrong. Final score: {score}")

    #make the game reaptable
    # making the account at position B become the next account at position A
    # clear the screan between round

