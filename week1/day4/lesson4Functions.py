# What is a FUNCTION? it is a SEQUENCE of ACTIONS that were given a name


#----------------------REUSABLE block of CODE that runs when you CALL it--------------------------

#Functions allow you to BREAK YOUR PROGRAMNS into SMALLER PARTS, each of which does one specific job.

# What is the FUNCTION SYNTAX?
#           def <function_name>(empty/arguments):          DEF calls the function
#                indented block of code                    BODY 
#           
#           call the function name()                       FUNCTION CALL

                               #SIMPLE FUNCTION EXAMPLE IN PRACTICE

def greetings():
    print("welcome, user!")

greetings()


#FUNCTION ARGUMENTS/PARAMETERS --> 
#------------------------------------1 ARGUMENT FUNCTIONS
def greetings(user_name):                 #user_name is the PARAMETER
    print(f"Welcome to the Good Place, {user_name}!")

greetings("Eleanor Shellstrop")   #Eleanor Shellstrop is the ARGUMENT
                                  #>>> Welcome to the Good Place, Eleanor Shellstrop!


def greetings(user_name = "Jason Mendoza"):
    print(f"Welcome to the Good Place, {user_name}!")

greetings()             #>>>Welcome to the Good Place, Jason Mendoza!



def greetings(user_name = "Jason Mendoza"):
    print(f"Welcome to the Good Place, {user_name}!")
greetings("Tahani Al Jamil")                 #<<<<Welcome to the Good Place, Tahani Al Jamil! 
#-------------------------------------------------"Tahani INSTEAD of Jason BECAUSE WE CHANGED THE ARGUMENT LATER!

#------------------------------------2 AND MORE ARGUMENT FUNCTIONS

#POSITIONAL ARGUMENTS/PARAMETERS

def say_hello(username, language):  # 2 POSITIONAL ARGUMENTS --> MANDATORY IN BOTH DEF AND CALL--------------------
    if language == "EN":
        print("Hello" + username)
    elif language == "FR":
        print("Bonjour" + username)
    else:
        print("This language is not supported: " + language)

say_hello("Rick", "FR")    #HAVE TO PASS 2 ARGUMENTS in the right order! 
                 #>>> Bonjour Rick


def greetings(user_name, language = "EN"):   #DEFAULT IN ENGLISH, IF LANGUAGE IS NOT SUPPORTED IN THE FUNCTION
    if language == "FR":
        print(f"Bienvenu, {user_name}")
    elif language == "PT":
        print(f"Bemvindo, {user_name}")
    elif language == "IT":
        print(f"Benvenuto, {user_name}")
    elif language == "UK":
        print(f"Laskavo prosimo, {user_name}")
    else: 
        print("Not supported language" + language)   #POSITIONAL!!!!!!!!!!!----------------------------------------------

greetings("Chidi Anagonye", "JP")          #>>> Not supported language JP

#KEYWORD ARGUMENTS/PARAMETERS
# Keyword arguments FREE YOU FROM ORDERING your arguments in the function call, clarifying the role of each value 
#                                                                                            in the function call.


#--------------CAREFUL: be sure to use the EXACT NAMES of the parameters in the function’s DEFINITION!!!!!!!!!!!!!!!!

def greetings(user_name, language = "EN"):   #DEFAULT IN ENGLISH, IF LANGUAGE IS NOT SUPPORTED IN THE FUNCTION
    if language == "EN" :
        print(f"Welcome, {user_name}")
    elif language == "PT":
        print(f"Bemvindo, {user_name}")
    elif language == "IT":
        print(f"Benvenuto, {user_name}")
    elif language == "UK":
        print(f"Laskavo prosimo, {user_name}")

greetings(language = "IT", user_name="Chidi Anagonye") # KW ARGUMENT name-value pair UNORDERED------------------
                                         #>>>Benvenuto, Chidi Anagonye


# You can use BOTH KW and POSITIONAL arguments in the same function call, but:
# ------------------------ 1)positional argument
#                          2) the keyword one

                                         

#MIXED ARGUMENTS (PARAMETERS)
def greetings(user_name, language = "EN"):   #DEFAULT IN ENGLISH, IF LANGUAGE IS NOT SUPPORTED IN THE FUNCTION
        print(f"Welcome, {user_name}")
    if language == "PT":
        print(f"Bemvindo, {user_name}")
    elif language == "IT":
        print(f"Benvenuto, {user_name}")
    elif language == "UK":
        print(f"Laskavo prosimo, {user_name}")
    else:
       print(f"Welcome, {user_name}")

greetings(language = "IT", user_name="Chidi Anagonye")

#EXERCISE # create a function called country_info that receives a country name as argument and prints the capital 
# of that country. Make the country name argument default
# Naboo (star wars planet). Its capital is Theed

def country_info(country = "Naboo"):
     if country == "Russia":
          print("Moscow")
        elif country == "Italy":
          print("Rome")
        elif country == "Brazil":
          print("Brazilia")
          elif country == "Naboo":
          print("Theed")

country_info()

#USING RETURN
#----------------If you want to USE THE RESULT of a function, you NEED return.
#---------------------------RETURNING ONLY 1 VALUE------------------------------------
#1)
def formatted_name(first_name, last_name):  #The function expects 2 ARGUMENTS
    full_name = first_name + ' ' + last_name   #other function that combines the 2 ARGUMENTS
    return full_name.title()                 #it RETURNS the combines 2 arguments CAPITALIZED (.title)

musician = formatted_name('jimi', 'hendrix')  #WE NEED THIS TO STORE THE RETURNED!!!!!!
                                              #MEANING, IT IS NOW STORED IN "musician"
print(musician)

#2)
def country_info(country = "Naboo"):   #if NO INPUT GIVEN, "Naboo" is DEFAULT
     if country == "Russia":
          capital = "Moscow"
          elif country == "Italy":
          capital = "Rome" 
          elif country == "Brazil":
          capital = "Brazilia"
          elif country == "Naboo":
          capital = "Theed"
     else:
          capital = "Unknown"
          return capital  # WITHOUT, the function does its work but DOES NOT GIVE ANYTHING BACK --> >>>"None"

print(country_info("Brazil"))

#---------------------------RETURNING MORE VALUES------------------------------------

def format_name(first_name, last_name):
    return (first_name.title(), last_name.title())  # WITHOUT, the function DOES NOT GIVE ANYTHING BACK

first, last = format_name("RICk", "mORTY")  #WE NEED THESE TO STORE THE RETURNED!!!!!!
print(first)
print(last)          # >>> Rick
                     # >>> Morty


