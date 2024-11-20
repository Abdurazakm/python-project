# print("\n__________________________________________________________________\nDAY FIVE\nFOR LOOP\n__________________________________________________________________\n")
# student_heights= input("input a list of student heights ").split()
# #exercise 1. on for loop to find average of student
# #given ----
# for n in range(0, len(student_heights)):
#     student_heights[n]=int(student_heights[n])
# print(student_heights)
# #--------------




# #my answer and teacher answer by using sum() len() function
# sum_of_students_height=sum(student_heights)
# num_of_students=len(student_heights)
# average_height = round(sum_of_students_height/num_of_students)
# print(num_of_students)
# print(average_height)
# #----------------------------


# #---------------------------------
# #this is teacher answer my answer almost the same with teacher answer
# total_height=0
# for height in student_heights:
#     total_height+=height
# number_of_students=0
# for student in student_heights:
#     number_of_students+=1
# average_of_student_heights=round(total_height/number_of_students)
# print(f"average of height of student = {average_of_student_heights}.")
# #---------------------------------------------

# #exercise 1. on for loop to find  of highest score of student
# #given ----
# student_score=input("Input a list of student score: ").split()
# for n in range(0, len(student_score)):
#     student_score[n]= int(student_score[n])
# print(student_score)
# #----------


# #answer
# highest_score=0
# for score in student_score:
#         if score>highest_score:
#             highest_score=score
# print(f"The highest score in the class is: {highest_score}")
# #--------


# #we can do by max() function to highest score and min() function to lowest score
# #simple---
# print(f"The highest score in the class is: {max(student_score)}")
# print(f"The lowest score in the class is: {min(student_score)}")





# #exercise on for loop with range to get sum of even number from 1 up to 100
# #-----
# sum_of_even_number=0
# for number in range(1,101):
#      if number%2==0:
#           sum_of_even_number+=number
# print(sum_of_even_number)
# #-----------
# #another way-----
# total=0
# for number in range(2,101,2):
#      total+=number
# print(total)
# #---------------------
     



# #exercise fizzBuzz game
# #-------------------------------------
# for number in range(1,100):
#      if number%3==0 and number%5==0:
#           print("FizzBuzz")
#      elif number %3==0:
#           print("Fizz")
#      elif number % 5==0:
#           print("Buzz")
     
#      else:
#           print(number)
# #-------------------------------------------




#day for final project which the write program which generate password with combination
# letter,number and symbols 
import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
         'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','^','&','*','(',')','+','_','-','/','<','>','? ']


print("Welcome to the password Generator!")
number_letters=int(input("How many letters would you like in your password?\n"))
number_symbols=int(input(f"How many symbols would you like?\n"))
number_numbers=int(input(f"How many numbers would you like?\n"))
# length_letters=len(letters)
# length_numbers=len(numbers)
# length_symbols=len(symbols)
# password=""
# for letter in range(0,number_letters):
#      random_choice1=random.randint(0,length_letters-1)
#      random_letters=letters[random_choice1]
#      password+=random_letters
# for number in range(0,number_numbers):
#      random_choice2=random.randint(0,length_numbers-1)
#      random_numbers=numbers[random_choice2]
#      password+=random_numbers
# for symbol in range(0,number_symbols):
#      random_choice3=random.randint(0,length_symbols-1)
#      random_symbols=symbols[random_choice3]
#      password+=random_symbols
# print(password)
# length_password=number_symbols + number_numbers + number_letters 

# combination_of_password=[password]
# print(len(password))
# last_password=""
# for len_password in range(0,len(password)):
#      random_password_choice=random.randint(0,len(password))
#      print(random_password_choice)
#      last_password += combination_of_password[random_password_choice-1]

# print(last_password)
     
     
password_list=[]
for letter in range(1,number_letters+1):
    password_list.append(random.choice(letters))
for number in range(1,number_numbers+1):
    password_list.append(random.choice(numbers))
for symbol in range(1,number_symbols+1):
    password_list.append(random.choice(symbols))
random.shuffle(password_list)
password=""
for char in password_list:
    password+=char
    
print(f"Your password is: {password}")
