# 1 Print the following output using one line of code: '''Hello world
#Hello world
#Hello world
#Hello world''''''

print('hello world\n'*4)

# 2 Write code that calculates the result of:
#(99^3)*8 (meaning 99 to the power of 3, times 8).

print((99^3)*8)

# 3 Predict the output of the following code snippets:
#Comment what is your guess, then run the code and compare

print(15 < 8) #False
print(3 == 3) #True
print(3 == "3") #False
print("3" > 3) #False -- actually not supported
print("Hello" == "hello") #False -- actually not supported

#4 Create a variable called computer_brand which value is the brand name of your computer.
# Using the computer_brand variable, print a sentence that states the following:
# "I have a <computer_brand> computer."

computer_brand = "HP"
print(f"I have a {computer_brand} computer.")

#5 Instructions
# Create a variable called name, and set it’s value to your name.
# Create a variable called age, and set it’s value to your age.
# Create a variable called shoe_size, and set it’s value to your shoe size.
# Create a variable called info and set it’s value to an interesting sentence about yourself. The sentence must contain all the variables created in parts 1, 2, and 3.
# Have your code print the info message.
# Run your code.

name = "Silvia"
age = "37"
shoe_size = "36"
info =f"My name is {name}, I am {age} years old, my shoe size is {shoe_size} and I was born on April 1st"
print(info)

#6 Create two variables, a and b.
# Each variable’s value should be a number.
# If a is bigger than b, have your code print "Hello World".

a = 3
b = 4
if a > b:
    print("Hello World")

#7 Write code that asks the user for a number and determines whether this number is odd or even.

number = int(input("Enter your number:"))
if number % 2 == 0:
    print("Your number is even")
else:
    print("Your number is odd")

#8 Write code that asks the user for their name and determines whether or not you have the same name. Print out a funny message based on the outcome.
user_name = input("What is your name? ")
my_name = "Silvia"
if user_name == my_name:
    print("Twinsies!")
else:
    print("Your name is not as cool as I thought it was gonna be...")

#9 Write code that will ask the user for their height in centimeters.
# If they are over 145 cm, print a message that states they are tall enough to ride.
# If they are not tall enough, print a message that says they need to grow some more to ride.

your_height = int(input("Enter your height in cms: "))
if your_height > 145:
    print("You are tall enough to ride this ride")
else:
    print("You have some more growing to do, shortie...")
