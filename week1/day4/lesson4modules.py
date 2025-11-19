#THIS IS AN EXAMPLE TAKEN FROM EXERCISE XP DAY 4

import random

def compare_num (user_num):
    comp_num = random.randint(1,100)
    if user_num == comp_num:
        print("You are a nandom number wizard!")
    else:
        print(f"No, this is the number of the computer {comp_num}, you failed!")

compare_num(55)

#THIS IS AN EXAMPLE TAKEN FROM EXERCISE XP DAY 7

def get_random_temp():                           #AUXILIARY FUNCTION TO HELP THE MAIN ONE, THE MAIN ONE WILL BE CALLED
    temp = random.randint(-10, 40)
    return temp #INSTEAD OF PRINT, YOU USE RETURN FOR TEMPS

def main_temp():
    temp = get_random_temp():
    if temp < 0:
