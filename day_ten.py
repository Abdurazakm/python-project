import os
def clear_console():
    # For Windows
        os.system('cls')
clear_console()
# #function with ouput
# def format_name(f_name,l_name):
#     #doc string meanse right after the definition of a function,method, class, or module.
#     #it is used to document the specific part of the code, providing a convenient way of associating documenatation 
#     #with python code
#     """Take a first and last name and format it
#     to return the title case version of the name"""
#     format_f_name=f_name.title()
#     format_l_name=l_name.title()
#     return f"{format_f_name} {format_l_name}"
# print(format_name("abdURAZak","MoHAMmeD"))
# #output=Abdurazak Mohammed


# def is_leap(year):
#   if year % 4 == 0:
#     if year % 100 == 0:
#       if year % 400 == 0:
#         return True
#       else:
#         return False
#     else:
#       return True
#   else:
#     return False

# def days_in_month(year,month):
#   if month>12 or month<1:
#     return "invalid month"
#   month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
#   if is_leap() and month==2:
#     return 29
#   return month_days[month-1]
# #🚨 Do NOT change any of the code below 
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)

# #--------------------------------------------------------------------------------------


#Todays project
#which is CALCULATOR

#addition
def add(num1,num2):
  return num1+num2

#subtraction
def substact(num1,num2):
  return num1-num2

#multiplication
def multiply(num1,num2):
  return num1*num2

#division
def divide(num1,num2):
  return num1/num2
def equal():
    return

operations={ "+":add,
            "-":substact,
            "*":multiply,
            "/":divide,
            "=":equal,
            }

def calculator():
    from calculator_art import logo
    print(logo)

    number1=float(input("What is the first number: "))
    for symbol in operations:
        print(symbol)

    calculating=True
    while calculating:
        operation_symbol=input("pick an operation: ")
        number2=float(input("What is the next number: "))

        calculation_funtion=operations[operation_symbol]
        answer=calculation_funtion(num1=number1,num2=number2)

        print(f"{number1} {operation_symbol} {number2} = {answer}")

        should_continue=input(f"Type 'y' to continue calculating with {answer}, type 'n' to start new calculation, type other key to exit.: ")

        if should_continue=='y':
            number1=answer

        elif should_continue=='n':
            calculating =False
            clear_console()
            calculator()

        else:
            calculating =False
calculator()
      
       

     
       













