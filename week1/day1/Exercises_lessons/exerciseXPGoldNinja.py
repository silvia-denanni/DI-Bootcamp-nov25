is_magician = False
is_expert = False
if is_magician and is_expert:
    print("you are a master magician!")
elif is_magician and not is_expert == False:
    print("you are on the right path!")
elif not is_magician:
    print("you too can become a magician if you train hard!")

print("Hello world\nHello world\nHello world\nHello world\nI love python\nI love python\nI love python\nI love python")

# 1
# Print the following output in one line of code:

# Hello world
# Hello world
# Hello world
# Hello world
# I love python
# I love python
# I love python
# I love python

print("Hello world", end=" ")
print("Hello world", end=" ")
print("Hello world", end=" ")
print("Hello world", end=" ")
print("I love python", end=" ")
print("I love python", end=" ")
print("I love python", end=" ")
print("I love python")

# 2
# Ask the user to input a month (1 to 12).
# Display the season of the month received :
# Spring runs from March (3) to May (5)
# Summer runs from June (6) to August (8)
# Autumn runs from September (9) to November (11)
# Winter runs from December (12) to February (2)

enter_month = int(input("Please enter a month in number format from 1 to 12: "))
if 3 <= enter_month <= 5:
    print("we are in Spring")
elif 6 <= enter_month <= 8:
    print("we are in Summer")
elif 9 <= enter_month <= 11:
    print("we are in Autumn")
elif enter_month == 12 or 1 <= enter_month <= 2:
      print("we are in Winter")
else:
    print("Please enter a month")

# 1 
# Run this command in the terminal to open a python console:
# $ python3

# 2
# Read about alias, and try to open a python console with the command:

# 3
# Predict the output of the following code snippets:

3 <= 3 < 9
3 == 3 == 3
bool(0)
bool(5 == "5")
bool(4 == 4) == bool("4" == "4")
bool(bool(None))

x = (1 == True)
y = (1 == False)
b = False + 10
a = True + 4
print("b:", b)
print("x is", x)
print("y is", y)
print("a:", a)

# 4
# Use python to find out how many characters are in the following text, use a single line of code (beyond the establishment of your my_text variable).
my_text = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
           sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
           Ut enim ad minim veniam, quis nostrud exercitation ullamco 
           laboris nisi ut aliquip ex ea commodo consequat. 
           Duis aute irure dolor in reprehenderit in voluptate velit 
           esse cillum dolore eu fugiat nulla pariatur. 
           Excepteur sint occaecat cupidatat non proident, 
           sunt in culpa qui officia deserunt mollit anim id est laborum.'''
print(len(my_text))

#5
#Keep asking the user to input the longest sentence they can without the character “A”.
# Each time a user successfully sets a new longest sentence, print a congratulations message

