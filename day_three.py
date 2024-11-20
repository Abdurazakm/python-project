#1 if condition
print("__________________________________________________________________\nlesson one if condition\n__________________________________________________________________\n")
print("well come to the rollcoster")
height=int(input("what is your height in cm: "))
if height>=120:
    print("you can ride rollcoster")
else:
    print("you have to grow toller before you can ride")







# excresice on if condition
print("\n__________________________________________________________________\nexcresice on if condition.\n check the number even or odd.\n__________________________________________________________________\n")

number=int(input("which number do you want to chack: "))
if number%2==0:
    print("This is a even number")
else:
    print("this is odd number")






#2 nested if/else statement
print("\n__________________________________________________________________\nlesson two nested if/else statement.\n__________________________________________________________________\n")
height=int(input("what is your height in cm?"))
if height>=120:
 print("you can ride rollcoster.")
 age=int(input("what is your age? "))
 if age<=18:
  print("please pay $7.")
 else:
    print("please pay $12.")
else:
   print("sorry, you have to grow taller before you can ride.")








#3 if/elif/else statement
print("\n__________________________________________________________________\nlesson three if/elif/else statement.\n__________________________________________________________________\n")
height=int(input("what is your height in cm?"))
if height>=120:
   print("you can ride rollcoster.")
   age=int(input("what is your age? "))
   if age<=10:
      print("please pay $5.")
   elif age<=15:
      print("please pay $7.")
   elif age<=18:
      print("please pay $10.")
   else :
      print("please pay $12.")
else:
   print("sorry, you have to grow taller befor you can ride.")







# excresice on if/elis/else statement
print("\n__________________________________________________________________\n1. excresice 2. on if/elis/else statement.\ninterpretation of their BMI based on the BMI value.\n__________________________________________________________________\n")
height=float(input("enter your height in m:"))
weight= float(input("enter your weight in kg:"))
BMI=round(weight/(height**2)) 
if BMI<18.5:
   print(f"your BMI is {BMI}, your are underweight.")
elif BMI>25:
   print(f"your BMI is {BMI}, your are normal weight.")
elif BMI<30:
   print(f"your BMI is {BMI}, your are overweight.")
elif BMI <35:
   print(f"your BMI is {BMI}, your are obese.")
else:
   print(f"your BMI is {BMI}, your are clinically obese.") 






print("\n__________________________________________________________________\n2. excresice 2.on if/elis/else statement.\nfind leap year?\nleap year is 366 day one extra day added in february month february month become 29 instead of 28.\n__________________________________________________________________\n")
year=int(input("which year do you want to check?"))
if year % 4==0:
      if year %100==0:
         if year %400==0:
            print("this year is leap year.")
         else:
            print("this year is not leap year.")
      else:
         print("this year is leap year.")

else:
      print("this year is not  leap year.")
   






#4 multiple if 
print("\n__________________________________________________________________\nlesson three if/elif/else statement.\n__________________________________________________________________\n")
height=int(input("what is your height in cm?"))
if height>=120:
   print("you can ride.")
   age=int(input("what is your age? "))
   bill=0
   if age<12:
      bill=5
      print("child ticket $5.")
   elif age >=18:
      bill =7
      print("youth ticket $7.")
#logical operatory
   elif age>=45 and age <=55:
      print("Everything is going to be ok. have a free ride on us. ")
   else:
      bill=12
      print("adult ticket $12.")
   wants_photo=input("do you want a photo taken? y or n: ")
   if wants_photo=="y":
      bill+=3
      print(f"your final bill is ${bill}.")
else:
   print("sorry, you have to grow taller befor you can ride.")







  # excrecise on multiple if
print("\n__________________________________________________________________\nexcrecise on multiple if.\n__________________________________________________________________\n")
print("Welcome to python pizza Delivary! ")
size=input("what size pizza do you want? s,m,l: ")
add_pepperani=input("Do you want pepperani? y,n: ")
extra_cheese = input("Do you want extra cheese? y,n: ")
bill=0
# pepperoni_bill=0
# # bill_of_extra_cheese=1

if size=="s":
   bill+=15
elif size=="m":
   bill+=20
elif size=="l":
   bill+=25
if add_pepperani=="y":
      if size=="s":
        bill+=2
      else:
          bill+=3
if extra_cheese=="y":
       bill+=1
print(f"your final bill is: ${bill}.")







#excrisice on logic operator
print("\n__________________________________________________________________\nexcrecise on logic operatore.\n__________________________________________________________________\n")
print("\n__________________________________________________________________\nWelocome to the love Calculatory!.\n__________________________________________________________________\n")
name1=input("What is your name?\n")
name2=input("What is your name?\n")
lower_name1=name1.lower()
lower_name2=name2.lower()
name=lower_name1 + lower_name2
print(name)
#TRUE LOVE  
count_t=name.count("t")
count_r=name.count("r")
count_u=name.count("u")
count_e=name.count("e")
true_count=count_t + count_r + count_u + count_e
count_l=name.count("l")
count_o=name.count("o")
count_v=name.count("v")
count_e=name.count("e")
love_count=count_l + count_o + count_v + count_e
true_love_score=int(str(true_count) + str(love_count))  
print(true_love_score)
if true_love_score< 10 or true_love_score > 90:
    print(f"Your score is {true_love_score},you go together like coke and mentos.")
elif true_love_score>=40 and true_love_score <=50:
    print(f"Your score is {true_love_score}, you are alright together.")
else:
    print(f"Your score is {true_love_score}.")
   


#FINAL PROJECT ON DAY THREE
print("\n__________________________________________________________________\nFINAL PROJECT ON DAY THREE.\n__________________________________________________________________\n")
print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
choice1=(input('You\'re at a cross road. Where do you want to go? Type "left" or "riht"\n')).lower()
if choice1=="left":
    choice2=(input('You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n')).lower()
    if choice2 =="wait": 
        choice3=(input('You arrive at the island unharmed. There is a house with 3 doors. one "red", one "yellow" and one "blue". Which colour do you choose?\n')).lower()
        if choice3=="red":
            print("It's a room full of fire. Game Over!")
        elif choice3=="yellow":
            print("You find the Treasure! You Win!")
        elif choice3=="blue":
            print("You enter the room of beasts. Game Over!")
        else:
            print("You choice  a door that doesn't exist. game over!")
    else:
        print("You got attacked by an angry trout,   game over!")
else:
    print("You fell into a hole, game over!")





    

      

