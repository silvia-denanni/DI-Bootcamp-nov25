# #STRINGS have "" or '' before the actual text. They are IMMUTABLE. 
# #STRING METHODS: .upper() ; .lower(). EX: 
# "SILVIA".lower()
# #>>>'silvia'
# len("Silvia")
# #>>>6
# type("12345")
# #>>><class 'str'>
# "5" + "2"
# #>>>'52'

# # STRINGS  are IMMUTABLE:
# my_name = "Silvia Denanni"
# my_name[0] = "G"
# print(my_name) 

# #>>>Traceback (most recent call last):
# #   File "<stdin>", line 1, in <module>
# # TypeError: 'str' object does not support item assignment
# # >>> print(my_name) 

# #SPECIAL CHARACTERS IN STRINGS: 
# # \t -> TO ADD A SPACE IN BTW WORDS (it DOES NOT WORK in the shell!) 
# # EX.

# #1) print("Juliana\tSchmidt")
# #>>> Juliana Schmidt

# #2) 
# # \n -> TO ADD A NEW LINE ->

# #sentence = "I love Python\t"
# #print(sentence*3)
# #>>>I love Python   I love Python   I love Python

# #3) 
# # sentence = "I love Python\n"
# # print(sentence*3)
# # >>>I love Python
# # I love Python
# # I love Python

# #  sentence = "I\'m in love with Python"
# # >>> print(sentence*3)
# # I'm in love with PythonI'm in love with PythonI'm in love with Python

# # sentence.replace("Python", "Javascript")
# #>>>"I'm in love with Javascript"

# sentence_js = sentence.replace("Python","Javascript")
# print(sentence_js)

# price = "15$"
# clean_price = price.replace("$", "")
# print(clean_price)
# # >>> 15

# price = "15$"
# clean_price = int(price.replace("$", ""))
# print(clean_price)
# # >>> 15

# #EXERCISE IN CLASS: make a string variable uppercase
# description = "strings are..."
# print(description.upper())
# #>>>STRINGS ARE...

# # replace a word in a string variable:
# new_description = description.replace("are","is")
# print(new_description)
# #>>>strings is...

# #STRING SLICING [:] this is to print only a part of a string. It uses the indexing concept, starting from 0. You can avoid writing it, as it follows:
# print(description[:7])
# >>>strings

# #NUMBERS: INTEGERS, FLOATS, COMPLEX
# #A division will always return a float in python. Ex.
# 5 + 5
# #>>>10
# 10/5  #this is an EXPRESSION
# #>>>2.0
# #To transform a string in a number we do like follows with function int():
#  int("5") + int("2")
# #>>>7
# #the other way round with string:
# type(str(25))
# #>>><class 'str'>

# #BOOLEANS: True(1)/False(0) values
# # >>> bool(0)
# # False
# # >>> bool(1)
# # True
# # >>>
# #also an empty string will give us 0
# # >>> bool()
# # False

# #NoneType: nothing, none

# #OPERATORS +,-,*,/(regular division),%(module, gives us the remaining number); ex:
# # 10%3
# # >>> 1


# # VARIABLES you can store values inside, whether integers, strings, booleans, etc.

# #VARIABLE NAMING BEST PRACTICES: 
# # NEVER START WITH NUMBERS OR SPECIAL CHARACTERS!!!!!!!!!!!
# # USE: SHORT NAMES, "_" for a space OR "-"
# # USE: lowercase
# #EXAMPLES ->

# #my_name = "Elettra"
# #my_name.upper()
# #>>>'ELETTRA'

# # name_upper = my_name.upper()
# my_name = "Silvia Denanni"
# print(name_upper)
# >>>SILVIA DENANNI


# #VARIABLES can be linked by commas, ex.
# name, age = "Elettra", 17

# # RULES:
# # variables don't store the expression, but the output of the expression

# calculation = 5+6
# print(calculation)


# #EXERCISE IN CLASS 
# #try to swap the values of x and y:
# x = 1
# y = 2
# #my code
# temp = y # we created a TEMPORARY VARIABLE to store the original one of x, so as not to lose it
# y = x
# x = temp
# print(x, y)
# #>>> x = 2
# y = 1

# #other way to do it:
# x,y = y,x
# print(x,y)

# #f STRINGS (f = format)

# user_name = input("Enter your name: ")
# print(user_name)
# age = int(input("Enter your age: "))
# print(age + 10)

# print(f"{user_name} is {age} years old.") #f STRING

# #INCREMENT a VARIABLE
# output = ""
# output += "J"
# print(output)

# # count = 0
# # >>> user_name = input("Enter your name: ")
# # Enter your name: count += 1
# # >>> count = 0
# # >>> my_name = input("Enter your name: ")
# # Enter your name: Silvia
# # >>> count+=1
# # >>> print(user_name)
# # count += 1
# # >>> print(count)
# # 1

# # CLASS EXERCISE: Ask the user for their age using the input() function and store it in a variable age.
# # Convert the inputted age into an integer and calculate the number of years until they turn 100.
# # Display a message: "You will turn 100 in X years", where X is the number of years calculated.

# your_age = int(input("What\'s your age? "))
# when_100 = 100 - your_age
# print(f"You will be 100 in {when_100} years.")

# # >>>What's your age? 23
# # >>> when_100 = 100 - your_age
# # >>> print(f"You will be 100 in {when_100} years.")
# # You will be 100 in 77 years.

# #CONDITIONALS, you use BOOLEANS and LOGIC OPERATORS (==, !=, <, >, <=, >=)
# #SYNTAX OF CONDITIONALS: 
# # if <condition>
# #    indented block 

from datetime import date


customer_age =int(input("What is your age? "))
if customer_age < 7:
  print("We will call your parents!!!")
elif customer_age <= 12:
  print("Sorry, you cannot watch the movie.")
elif customer_age <= 13 and customer_age <= 16: # OR customer_age >= 13 and customer_age <= 16
  print("You can only watch the movie with a legal guardian.")
else:
  print("You are free to watch the movie on your own!")

birth_year = int(input("When were you born? "))
your_age = 2025 - birth_year
print(f"Your age is {your_age}")

#Bonus: Calculate Age Dynamically Using the "datetime" module --> date.today().year for 2025
birth_year =int(input("When were you born? "))
current_year =date.today().year
your_age =current_year - birth_year
print(f"Your age is {your_age}")