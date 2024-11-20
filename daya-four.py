# # #merssine twister
# # #search in askpythone.com for pythone random module
# # print("\n__________________________________________________________________\nDAY FOUR\nRandom number generetor\n__________________________________________________________________\n")
# # import random
# # random_int=random.randint(1,10)
# # print(f"Random intiger number generator generats {random_int}")
# # random_float=random.random()
# # print(f"Random float number generator generats {random_float}")


# # print("\n__________________________________________________________________\nRandom number generetor\nHEADS AND TAILS exeresice \n__________________________________________________________________\n")
# # random_side=random.randint(0,1)
# # if random_side==1:
# #     print("Head")
# # else:
# #     print("Tail")





# # # print("\n__________________________________________________________________\nExeresice on list\nfind random name then who have to buy the meal for all \n__________________________________________________________________\n")
# # # import random
# # # names_string = input("Give me everybody's names, seperated by a comma. ")
# # # names=names_string.split(", ")
# # # num_items=len(names)
# # # random_choice=random.randint(0,num_items-1)
# # # person_who_will_pay=names[random_choice]
# # # print(person_who_will_pay + " is going to buy the meal today!")


# # #we can do and perform this task by another way
# # #which is by using choice() function the below two code line perform this
# # # person_who_will_pay=random.choice(names)
# # # print(person_who_will_pay + " is going to buy the meal today!")

# # print("\n__________________________________________________________________\nExeresice  \n__________________________________________________________________\n")
# # row1=["😀","😁","😅"]
# # row2=["🥶","😱","👿"]
# # row3=["🙂","🥰","🤪"]
# # map=[row1,row2,row3]
# # print(f"{row1}\n{row2}\n{row3}")
# # position=input("Where do youwnat to put the treasure? ")
# # position_x=int(position[0])
# # position_y=int(position[1])
# # if position_x==3 and position_y==3:
# #  map[position_x-1][position_y-1]="x"
# # elif position_x==3:
# #  map[position_x-1][position_y]="x"
# # elif position_y==3:
# #  map[position_x][position_y-1]="x"
# # else:
# #   map[position_x][position_y]="x"
  
# # print(f"{row1}\n{row2}\n{row3}")



# print("\n__________________________________________________________________\nDAY FOUR PROJECT\n__________________________________________________________________\n")
import random
rock = '''
    ______
---' (_____)
      (_____)
      (_____)
      (____)
---'_(___)
       
'''
paper = '''
    ______
---'______)__
    _________)
    __________)
    _______)
---'______)
       
'''
scissors='''
     ____
---' (____)___
      _________)
      ________)
      (______)
---'__(___)
       
'''
#my answer for project
# rock_paper_scissor_play=[rock,paper,scissors]
# computer_choose=random.randint(0,2)
# person_choose=int(input("What Do You choose? Type 0 for, Rock, 1 for Paper or 2 for Scissors."))
# if person_choose==0 and computer_choose ==1:
#   print(f"Your choose\n{rock}\ncomputer choose\n{paper}\nYOU LOSE!")
# elif person_choose==1 and computer_choose ==0: 
#   print(f"Your choose\n{paper}\ncomputer choose\n{rock}\nYOU WIN!")
# elif person_choose==0 and computer_choose ==2:
#   print(f"Your choose\n{rock}\ncomputer choose\n{scissors}\nYOU WIN!")
# elif person_choose==2 and computer_choose ==0:
#   print(f"Your choose\n{scissors}\ncomputer choose\n{rock}\nYOU LOSE!")
# elif person_choose==1 and computer_choose ==2:
#   print(f"Your choose\n{paper}\ncomputer choose\n{scissors}\nYOU LOSE!")
# elif person_choose==2 and computer_choose ==1:
#   print(f"Your choose\n{scissors}\ncomputer choose\n{paper}\nYOU WIN!")
# elif person_choose==computer_choose:
#    if person_choose==0:
#     print(f"Your choose\n{rock}\ncomputer choose\n{rock}\nTHE GAME IS TIE")
#    elif person_choose==1:
#     print(f"Your choose\n{paper}\ncomputer choose\n{paper}\nTHE GAME IS TIE")
#    elif person_choose==2:
#     print(f"Your choose\n{scissors}\ncomputer choose\n{scissors}\nTHE GAME IS TIE")
# else:
#   print("INVALID CHOOSE")


#teacher answer answer for project
game_image=[rock,paper,scissors]
users_choose=int(input("What Do You choose? Type 0 for, Rock, 1 for Paper or 2 for Scissors."))
if users_choose >=3 or users_choose < 0:
  print("INVALID CHOICE")
else:
  print(f"YOUR CHOSE\n{game_image[users_choose]}")
  computer_choose=random.randint(0,2)
  print(f"computer choice\n{game_image[computer_choose]}")
  if computer_choose==0 and users_choose==2:
    print("YOU LOSE")
  elif users_choose==0 and computer_choose==2:
    print("YOU WIN")
  elif computer_choose> users_choose:
    print("YOU LOSE")
  elif users_choose>computer_choose:
   print("YOU WIN")
  elif computer_choose==users_choose:
    print("It's a DRAW")  
   




  
  
  

 







