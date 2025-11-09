#FUNCTIONS to call them, you need "function name" (in the following example "hello"):
def hello():
    print("Hello World!")
hello()

#FUNCTIONS: or you need to use "return" to call them:
# def hello():
#     return ("Hello World!")
# print(hello())
#FUNCTIONS: another example
# def introduce_pets(cat_name, lion_name):
#     return f"My cats are called {cat_name} and {lion_name}!"
# print(introduce_pets("Buffy", "Tuli"))
# print(introduce_pets('Mayo', 'Naise'))

def greet_person (name, age):
    return(f"Hello {name}, you are {age}.")
print(greet_person("Alice", 30))

#FUNCTIONS: in the following case, you can define a parameter as default ("age" in the following example):
def greet_person (name, age=25):
    return(f"Hello {name}, you are {age}.")
print(greet_person("Bob"))

#GLOBAL VARIABLES: use of the "global" keyword to call it inside a function:
counter = 0
def increment_global_counter():
    global counter
    counter += 1
increment_global_counter()
print(counter)


def add_two_numbers(a, b):
    return a + b
print(add_two_numbers(3, 5))

even_odd =int(input("Insert a number and I will tell you if it is even or odd: "))
if even_odd % 2 == 0:
    print("Even")
else:
    print("Odd")

def greet(name):
    return (f"Hi {name}!")
print(greet("Alice"))

#Write a function sum_list that takes a list of numbers as a parameter and returns the sum of all numbers in the list.
def sum_list (numbers):
    return sum(numbers)
print(sum_list([2,3,4,5]))

#Write a function print_days that prints the days of the week (Sunday, Monday, Tuesday, etc.) using a loop.

def print_days ():
    days = [("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday","Sunday")]
for day in days:
    print(day)
print(print_days)

#Write a function repeat_word that takes a word and a number as parameters and prints the word that many times.
def repeat_word(word, times):
    for _ in range(times):
        print(word)
repeat_word("goodbye", 2)