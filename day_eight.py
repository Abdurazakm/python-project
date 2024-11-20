# #function with inputs
# #argument and parameters
# #simple function
# def greet():
#     print("Hello everyone")
#     print("How do you do?")
#     print("is'nt nice weather todey?")

# greet()
# #function with input
# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
# greet_with_name("abdurazak")
# #function with more than input
# def greet_with_more_input(name,location):
#     print(f"Hello {name}")
#     print(f"What is it in {location}?")
# #positional argument
# greet_with_more_input("abdurazak", "Hawassa")
# #key word argument
# greet_with_more_input(location="Nowhere",name="abdurazak")




# #Write your code below this line 👇
# import math
# def paint_calc(height,width,cover):
#     area=(height*width)
#     num_cans=area/cover
#     round_up_cans=math.ceil(num_cans)
#     print(f"You'll need {round_up_cans} cans of paint.")
# #Write your code above this line 👆
# # Define a function called paint_calc() so that the code below works.   

# # 🚨 Don't change the code below 👇
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)



# #Write your code below this line 👇
# def prime_checker(number):
#     check=False
#     num=number
#     count=0
#     while not check:
#         if num==0:
#          check=True
#          print("the number is prime")
#         elif number%num==0:
#             count+=1
#             if count>=3:
#                 check=True
#                 print("The number is not prime.")
#         num-=1
           
# #Write your code above this line 👆
    
# #Do NOT change any of the code below👇
# n = int(input("Check this number: "))
# prime_checker(number=n)


#day eight project--------------------------------------------------------------------------------------------
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def caesar(strat_text,shift_amount,cipher_direction):
    end_text=""
    if cipher_direction=="decode":
        shift_amount*=-1
    for letter in strat_text:
        if letter not in alphabet:
            end_text+=letter
        else:
            position=alphabet.index(letter)
            new_position=position+shift_amount
            new_letter=alphabet[new_position]
            end_text+=new_letter
    print(f"Here's the {cipher_direction}d result: {end_text}")

#TODO-1: Import and print the logo from art.py when the program starts.
from cipher_art import logo
print(logo)
#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 
should_end=False
while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    #TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
    #Try running the program and entering a shift number of 45.
    #Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
    #Hint: Think about how you can use the modulus (%).
    shift=shift%26
    caesar(strat_text=text,shift_amount=shift,cipher_direction=direction)
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")
    







