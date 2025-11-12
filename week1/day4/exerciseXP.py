#1 What Are You Learning? Create a function that displays a message about what you’re learning.

def display_message():
    print("I am learning about functions in Python.")
display_message()

#2 What’s Your Favorite Book? Create a function that displays a message about a favorite book.

def fav_book(title):
    print(f"One of my favorite books is {title}")

fav_book("Perfume")

#3 Some Geography --> Create a function that describes a city and its country.

def describe_city(city , country = "Unknown"):
    city_is = f"{city} is in {country}"
    return city_is

print(describe_city(city = "Sassari", country = "Italy"))

#4 Random --> Create a function that generates random numbers and compares them
import random

def compare_num (user_num):
    comp_num = random.randint(1,100)
    if user_num == comp_num:
        print("You are a nandom number wizard!")
    else:
        print(f"No, this is the number of the computer {comp_num}, you failed!")

compare_num(55)

#5 Let’s Create Some Personalized Shirts! Create a function to describe a shirt’s size and message, 
# with default values.

def make_shirt(size = "large", text = "I love Python"):
    tshirt_desc = f"The tshirt is size {size} and it features this print: {text}"
    return tshirt_desc

make_shirt() # Call make_shirt() to make a large shirt with the default message.
make_shirt(size = "medium") # Call make_shirt() to make a medium shirt with the default message.
make_shirt(size = "any size", text = "If cats could speak to you, they would not")



#6 Magicians…  Modify a list of magician names and display them in different ways.

magician_names = ["Harry Houdini", "David Blaine", "Criss Angel"]

def show_magicians(magician_names):
    for name in magician_names:
        print(name)

show_magicians(magician_names)

def make_great(magician_names):
    for name in (magician_names):
        print(f"the Great {name}")    

make_great(magician_names)


#7 Temperature Advice --> Generate a random temperature and provide advice based on the temperature range.
# STEP 1 ONLY
import random
def get_random_temp():    
    temp = random.randint(-10, 40)
    return temp # return is to call the random temp

get_random_temp()

# STEP 2 ONLY
import random
def get_random_temp():    #AUXILIARY FUNCTION TO HELP THE MAIN ONE, THE MAIN ONE WILL BE CALLED
    temp = random.randint(-10, 40)
    return temp # return is to call the random temp

def main_temp():
    print (f"The temperature right now is {get_random_temp()} Celsius.")
    return get_random_temp

main_temp()

# STEP 3 ONLY
import random

def get_random_temp():
    temp = random.randint(-10, 40)
    return temp

def main_temp():
    current_temp = get_random_temp()
    print(f"The temperature right now is {current_temp} Celsius.")
    return current_temp


temp = main_temp()  # Call main_temp and get the temperature value

if temp < 0:
    print("Brrr, that\'s freezing! Wear some extra layers today.")
elif 0 <= temp < 16:
    print("Quite chilly! Don\'t forget your coat.")
elif 16 <= temp <= 23:
    print("Nice weather.")
elif 24 <= temp <= 32:
    print("A bit warm, stay hydrated.")
elif 32 < temp <= 40:
    print("It\'s really hot! Stay cool.")


