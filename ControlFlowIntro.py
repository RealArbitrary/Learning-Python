#Booleans with Python
#Determine if the following statements are boolean expressions or not. If they are, set the matching variable to the right to "Yes" and if not set the variable to "No"
#My dog is the cutest dog in the world.
example_statement = "No"
#Dogs are mammals.
statement_one = "Yes"
#My dog is named Pavel.
statement_two = "Yes"
#Dogs make the best pets.
statement_three = "No"
#Cats are female dogs.
statement_four = "Yes"
#*********************************************************************************************
#Relational Operators: Equals and Not Equals
#(5 * 2) - 1 == 8 + 1
statement_one = True
#13 - 6 != (3 * 2) + 1
statement_two = False
#3 * (2 - 1) == 4 - 1
statement_three = True
#*********************************************************************************************
#Boolean Variables
#Create a variable named my_baby_bool and set it equal to "true"
my_baby_bool = "true"
#Check the type of my_baby_bool using type(my_baby_bool).
#You’ll have to print it to get the results to display in the terminal.
print(type(my_baby_bool))
#It’s not a boolean variable! Boolean values True and False always need to be capitalized and do not have quotation marks.
#Create a variable named my_baby_bool_two and set it equal to True.
my_baby_bool_two = True
#Check the type of my_baby_bool_two and make sure you successfully created a boolean variable.
#You’ll have to print it to get the results to display in the terminal.
print(type(my_baby_bool_two))
#*********************************************************************************************
#If Statement
#**The example**
#user_name = 
#if user_name = "Dave":
#  print("Get off my computer Dave!")
#**End Of The example**
#In script.py, there is an if statement. I wrote this because my coworker Dave kept using my computer without permission and he is a real doofus. If the user_name is Dave, it tells him to stay off my computer.
#Enter a user name in the field for user_name and try running the program.
user_name = ""
#Oh no! We got a SyntaxError! This happens when we make a small error in the syntax of the conditional statement.
#Read through the error message carefully and see if you can find the error. Then, fix it, and run the code again.
if user_name == "Dave":
  print("Get off my computer Dave!")
#Ugh! Dave got around my security and has been logging onto my computer using our coworker Angela’s user name, angela_catlady_87.
#Set your user_name to be angela_catlady_87.
#Update the program with a second if statement so it checks for Angela’s user name as well and prints
#"I know it is you, Dave! Go away!"
#in response. That’ll teach him!
if user_name == "angela_catlady_87":
  print("I know it is you, Dave! Go away!")
#*********************************************************************************************
#Relational Operators II
x = 20
y = 20
credits = 120
#Create an if statement that checks if x and y are equal, print the string below if so:
#"These numbers are the same"
if x == y:
  print("These numbers are the same")
#The nearby college, Calvin Coolidge’s Cool College (or 4C, as the locals call it) requires students to earn 120 credits to graduate.
#Write an if statement that checks if the student has enough credits to graduate. If they do, print the string:
#"You have enough credits to graduate!"
#Can a student with 120 credits graduate from Calvin Coolidge’s Cool College?
if credits >= 120:
  print("You have enough credits to graduate!")