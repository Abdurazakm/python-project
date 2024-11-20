# import os
# os.system('cls')
# #dubugging the bug
# #1 SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
# number=int(input("which number do you want to check? "))
# if number%2=0:
#    print("this number is an even number.")
# else:
#    print("this number is an odd number.")




 
# #2 TypeError: not all arguments converted during string formatting
# #solution we have to change str to int data type year=(input("which year do you want to check? "))
# year=(input("which year do you want to check? "))

# if year % 4==0:
#    if year % 100==0:
#       if year%400==0:
#        print("leap year.")
#       else:
#          print("Not leap year.")
#    else:
#       print("leap year.")
# else:
#    print("not leap year.")



import day_fifteen

print(day_fifteen.MENU["espresso"])
       

# for number in range(1,101):
#     if number % 3==0 and number % 5==0:
#         print("Fizzbuzz")
#     elif number % 3 ==0:
#         print("Fizz")
#     elif number % 5==0:
#         print("Buzz")
#     else:
#         print(number)