import os
def clear_console():
    # For Windows
        os.system('cls')
clear_console()
#dictionary in python
programming_dictionary={
    "Bug": "An error in a progran that prevents the program from running as expected.",
    "function": "A piece of code that you can easly call over and over again.",
}
#retrieving items from dictionary.
#simple
print(programming_dictionary["Bug"])
#adding new items to dictionary
programming_dictionary["Loop"]="The action of doing something over and over again. ",
#edit an item in a dictionary
programming_dictionary["Bug"]="A moth in your computer."
#loop through a dictionarly
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
#creaate an empty dictionary
empty_dictionary={}
#wipe an existing dictionary
programming_dictionary={}



#exercise
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades={}
#TODO-2: Write your code below to add the grades to student_grades.👇
for student in student_scores:
    score=student_scores[student]
    if score>90: 
        student_grades[student]="Outstanding"
    elif score>80:
        student_grades[student]="Exceeds Expectations"
    elif score>70:
        student_grades[student]="Acceptable"  
    else:
        student_grades[student]="Fail"
# 🚨 Don't change the code below 👇
print(student_grades)

#nested dictionary
capital={"frence": "paris",
         "germenry":"berlin"}
#nesting a list in a dictionary
travels_log={"Frence":["paris","Lille","Dijon",],
             "Germany":["Berlin","Hamburg","stuttgar"],
             }
#nesting dictionary in a dictionary 
travels_log={"Frence":{"cities_visited":["paris","Lille","Dijon",],"total_viseted":12},
             "Germany":{"cities_visited":["Berlin","Hamburg","stuttgar"],"total_viseted":5},
             }
#nesting dictionary in a list
travels_log=[
        {"country":"Frence",
        "cities_visited":["paris","Lille","Dijon",],
        "total_viseted":12
        },
        {"country":"Germany",
            "cities_visited":["Berlin","Hamburg","stuttgar"],
            "total_viseted":5
            },
            ]


# -----------------------------------------------
# exercise on nested dictionary in a list 
# add new list
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(country_visited,time_visited,cities_visited):
    new_country={}
    new_country["country"]=country_visited
    new_country["visits"]=time_visited
    new_country["cities"]=cities_visited
    travel_log.append(new_country)
# #🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)





# --------------------------------------------------------------------------------------------------------------
#DAY NINE PROJECT--------------
from Blind_Auction import logo
print(logo)
bids = {}
bidding_finished = False
def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")
print("Welcome to the secret auction program.")
while not bidding_finished:
    name=input("What is your name?: ")
    price=int(input("What's your bid?: $"))
    bids[name]=price
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if should_continue == "no":
        bidding_finished = True
        clear_console()
        find_highest_bidder(bids)
    elif should_continue == "yes":
        clear_console()






            





