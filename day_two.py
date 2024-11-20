# day two

# data type 

# string 
# print("hello"[0])

# #intiger

# print(123+456)

# write  a program that add the digit in a 2 digit 
# number e.g it the input was 35 then the output should be 3+5=8
two_digit_number=input("enter two digit number: ")
print(type(two_digit_number)) #to know which data type is
# get the first and xecond digits using subscripting then convert string to int.
first_number=int(two_digit_number[0])
second_number=int(two_digit_number[1])
# add two digit
sum=first_number + second_number
print(sum)
# to calculat BMI
height=input("enter your height in m ")
weight=input("enter the your weight in kg ")
height_in_to_float=float(height)
weight_in_to_int=int(weight)
# calculat like this
BMI=(height_in_to_float/weight_in_to_int**2)
print(BMI)
# convert bmi in to int
BMI_in_to_int=int(BMI)
print(BMI_in_to_int)
# creat a program using maths and f_string that tell us
# how many days,weeks,months,we have left if we live until 90 years old
age=input("what is your current age: ")
current_age=int(age)
remainig_age= 90-current_age
remaining_day=365*remainig_age
week=remainig_age*52
month=remainig_age*12
# f_string
message=f"you have {remaining_day} Days, {week} weeks and {month} months left."
print(message)

# DAY TWO FINALLY PROJECT
print("Welcome to the tip calcutor")
bill=float(input("what was the total bil? $"))
tip=int(input("what perecentage tip would you like to give? 10,12, or 15? "))
num_of_people=int(input("how many people to split the bill? "))
tip_as_perecent=tip/100
total_tip_amount=bill*tip_as_perecent
total_bill=total_tip_amount+bill
bill_per_person=total_bill/num_of_people
final_bill=round(bill_per_person,2)
# altarnative to round in to two decimal place
final_bill="{:.2f}".format(bill_per_person)

print(f"Each person should pay: ${final_bill}")





