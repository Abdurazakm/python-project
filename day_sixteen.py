# from turtle import Turtle,Screen
# timmy=Turtle()
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)
# timmy.backward(100)
# print(timmy)
# my_screen=Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()





from prettytable import PrettyTable

# Create a PrettyTable object
table = PrettyTable()
table.add_column("Pokemon name", ["pikachu","Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])
#if we want to align to left hand margin we use align feild name like table.align = "l",for right hand "r", for center "c"
table.align="l"

# # Define the column names
# table.field_names = ["Name", "Age", "Occupation"]

# # Add rows of data
# table.add_row(["Alice", 30, "Engineer"])
# table.add_row(["Bob", 24, "Designer"])
# table.add_row(["Charlie", 28, "Doctor"])

# # Print the table
print(table)
# table.=["first name","last name","age"]

