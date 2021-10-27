#Great job! We covered a ton of material in this lesson and we’ve increased the number of tools in our Python toolkit by several-fold. Let’s review what we’ve learned this lesson:
#Boolean expressions are statements that can be either True or False
#A boolean variable is a variable that is set to either True or False.
#We can create boolean expressions using relational operators:
#==: Equals
#!=: Not equals
#>: Greater than
#>=: Greater than or equal to
#<: Less than
#<=: Less than or equal to
#if statements can be used to create control flow in your code.
#else statements can be used to execute code when the conditions of an if statement are not met.
#elif statements can be used to build additional checks into your if statements
#Let’s put these skills to the test!
print("I have information for the following planets:\n")

print("   1. Venus   2. Mars    3. Jupiter")
print("   4. Saturn  5. Uranus  6. Neptune\n")
 
weight = 185
#This didn't want to work on the CodeCademy editor, but I wanted to take in an input to ask Codey which planet he was on
#planet = input("What planet are you on?")
planet = 5
# Write an if statement below:
if planet == 1:
  weight = weight / 0.91
  planet = "Venus"
elif planet == 2:
  weight = weight / 0.38
  planet = "Mars"
elif planet == 3:
  weight = weight / 2.34
  planet = "Jupiter"
elif planet == 4:
  weight = weight / 1.06
  planet = "Saturn"
elif planet == 5:
  weight = weight / 0.92
  planet = "Uranus"
else:
  weight = weight / 1.19
  planet = "Neptune"

print("Welcome to", planet, "your weight here is: ", weight)