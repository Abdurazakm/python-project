logo='''
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
'-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
      |  \/ K|                            _/ |                
      '------'                           |__/           
    
                                                                               '''
import random
# from blackjack_art import logo
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
# def player(player_card,sum_of_player,computer_card,sum_of_computer, another_card):
#     chosen_card=random.choice(cards)
#     sum_of_player+=chosen_card
#     player_card.append(chosen_card)
#     if sum_of_player>21:
#         print(f"Your final hands: {player_card}, final score: {sum_of_player}")
#         print(f"Computer final hand: {computer_card}, final score: {sum_of_computer}")
#         print("You want over. You lose!")
#         another_card=False
# def dealer(chosen_card_for_computer):
#     return 
# def blackjack():
#     player_card=[]
#     sum_of_player=0
#     sum_of_computer=0
#     computer_card=[]
#     looping=2
#     another_card=False
#     # while not another_card:
#     for _ in range(2):
#         chosen_card_for_player=random.choice(cards)
#         chosen_card_for_computer=random.choice(cards)
#         print(chosen_card_for_computer)
#         sum_of_player+=chosen_card_for_player
#         player_card.append(chosen_card_for_player)
#         computer_card.append(chosen_card_for_computer)
#         sum_of_computer+=chosen_card_for_computer
#         if 11 and 10 in computer_card:
#             print("you lose")
#         elif 11 and 10 in player_card:
#             print("you win")
#     print(f"Your cards: {player_card}, current score: {sum_of_player}")
#     print(f"Computer's first card: {chosen_card_for_computer}")
#     if sum_of_player>21:
#         if 11 in player_card:
#             sum_of_player-10

#         print(f"Your final hands: {player_card}, final score: {sum_of_player}")
#         print(f"Computer final hand: {computer_card}, final score: {sum_of_computer}")
#         print("You want over. You lose!")
#     else:
#         again=input("Type 'y' to get another card, type 'n' to pass: ")
#         if again=="y":
#             player(player_card,sum_of_player,computer_card,sum_of_computer, another_card)
#         elif again=="n":
#             another_card=True
#             dealer(chosen_card_for_computer)
# should_play=False
# while not should_play:
#     should_countine=input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
#     if should_countine=="n":
#         should_play=True
#     elif should_countine=="y":
#         print(logo)
#         blackja








def dealer_card(user, computer):
    less_than_17 = True
    while less_than_17:
        t_user = sum(user)
        t_computer = sum(computer)
        if t_computer < 17:
            computer.append(random.choice(cards))
        else:
            less_than_17 = False
            if t_user > t_computer:
                who_win = "you win"
            elif t_user < t_computer:
                who_win = "you lose"
            else:
                who_win = "drawn"
            print(f"Your final hands: {user}, final score: {t_user}")
            print(f"Computer final hand: {computer}, final score: {t_computer}")
            print(f"Game over. {who_win}")

def calculator_score(user, computer):
    total_score_of_user = sum(user)
    total_score_of_computer = sum(computer)
    print(f"Your card: {user}, current score: {total_score_of_user}")
    print(f"Computer's first card: {computer[0]}")
    
    if 11 in computer and 10 in computer:
        who_win = "you lose"
        print(f"Your final hands: {user}, final score: {total_score_of_user}")
        print(f"Computer final hand: {computer}, final score: {total_score_of_computer}")
        print(f"Game over. {who_win}")
        return who_win
    elif 11 in user and 10 in user:
        who_win = "you win"
        print(f"Your final hands: {user}, final score: {total_score_of_user}")
        print(f"Computer final hand: {computer}, final score: {total_score_of_computer}")
        print(f"Game over. {who_win}")
        return who_win
    else:
        if total_score_of_user > 21:
            if 11 in user:
                user[user.index(11)] = 1
                total_score_of_user = sum(user)
                if total_score_of_user > 21:
                    who_win = "you lose"
                    print(f"Your final hands: {user}, final score: {total_score_of_user}")
                    print(f"Computer final hand: {computer}, final score: {total_score_of_computer}")
                    print(f"Game over. {who_win}")
                    return who_win
            else:
                who_win = "you lose"
                print(f"Your final hands: {user}, final score: {total_score_of_user}")
                print(f"Computer final hand: {computer}, final score: {total_score_of_computer}")
                print(f"Game over. {who_win}")
                return who_win

def blackjack():
    draw_another_card = True
    user = []
    computer = []
    who_win = "you win"
    for _ in range(2):
        user.append(random.choice(cards))
        computer.append(random.choice(cards))
    return_value = calculator_score(user, computer)
    if return_value == "you lose" or return_value == "you win":
        draw_another_card = False
    else:
        draw_another_card = True
    while draw_another_card:
        should_again = input("Type 'y' to get another card, type 'n' to pass: ")
        if should_again == "y":
            user.append(random.choice(cards))
            return_value = calculator_score(user, computer)
            if return_value == "you lose" or return_value == "you win":
                draw_another_card = False
        else:
            draw_another_card = False
            dealer_card(user, computer)

should_play = False
while not should_play:
    should_continue = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if should_continue == "n":
        should_play = True
    elif should_continue == "y":
        import os
        print(os.system('cls'))
        print(logo)
        blackjack()











        
