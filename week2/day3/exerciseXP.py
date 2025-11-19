#Exercise 1: Currencies
# USE --->
# Dunder methods (__str__, __repr__, __init__, __add__, __iadd__)
# Type checking (isinstance())
# Raising exceptions (raise TypeError)

class Currency:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency
        
    def __str__(self):
        return f"{self.amount} {self.currency}"

    def __repr__(self):
        return f"{self.amount} {self.currency}"           # WHAT the object IS and what data it HOLDS

    def __int__(self):
        return int(self.amount)
    
    def __add__(self, other):
        if isinstance(other, int):                                      #this is the right syntax for the dunder
            return Currency(self.amount + other, self.currency)        #add integer to amount
        elif isinstance(other, Currency):
            if self.currency == other.currency:
                return Currency(self.amount + other.amount, self.currency) # add ONLY if same currency type
            else:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
        else:
            return NotImplemented
        
    def __iadd__(self, other):        #supports in-place addition (+=)
        if isinstance(other, int):
            self.amount += other
            return self
        elif isinstance(other, Currency):
            if self.currency == other.currency:
                self.amount += other.amount
                return self
            else:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")   #Adding different currency types raises a TypeError
        else:
            return NotImplemented

c1 = Currency(5, 'dollars')
c2 = Currency(10,'dollars')
c3 = Currency(1,'shekels')
c4 = Currency(10,'shekels')

print(c1)
# '5 dollars'

print(int(c1))
# # 5

print(repr(c1))
# '5 dollars'    # clear, useful string INSTEAD of GENERIC reply <Currency object at 0x...>

print(c1 + 5)
# 10             #it comes from __add__ --> we get a regular addition (+) result, a NEW OBJECT, the addends unchanged

print(c1 + c2)   #it comes from __add__ --> we get a regular addition (+) result, a NEW OBJECT, the addends unchanged
# 15

print(c1) 
# 5 dollars

c1 += 5          #it comes from __iadd__ --> in-place addition, modifies the original object itself and returns it
print(c1)            #after the addition, the value inside c1 changes 
# 10 dollars


c1 += c2         #it comes from __iadd__ --> in-place addition, modifies the original object itself and returns it
print(c1)            #after the addition, the value inside c1 changes
# 20 dollars

print(c1 + c3)  
#TypeError: Cannot add between Currency type <dollars> and <shekels>



#Exercise 2: Import   --> see files "function.py" and "exercise_one"



#Exercise 3: String module
import string 
import random

string = string.ascii_lowercase            # 'abcdefghijklmnopqrstuvwxyz'
random_chars = ""                          #  empty container for the 5 random letters

for num in range(5):
    random_char = random.choice(string)    # pick one random character
    random_chars += random_char            # add it to the result string

print(random_chars)



#Exercise 4: Current Date

import datetime

current_date = datetime.datetime.today()
print(current_date)    # 2025-11-18 23:13:40.925953



#Exercise 5: Amount of time left until January 1st

import datetime

current_date = datetime.datetime.today()    # 2025-11-18 23:13:40.925953

jan_date = datetime.datetime(2026, 1, 1)

print(jan_date)                             #2026-01-01 00:00:00

time_till_jan_date = jan_date - current_date

print(time_till_jan_date)   # 43 days, 0:42:04.907039


#Exercise 6: Birthday and minutes

from datetime import datetime

def minutes_lived(birthdate_str):                  # transforms birthdate STRING into a DATE OBJECT
    birthdate = datetime.strptime(birthdate_str, "%d-%m-%Y")     # that Python can work with
    
    now = datetime.now()

    time_lived = now - birthdate

    minutes = int(time_lived.total_seconds() / 60)

    print(f"You have lived approximately {minutes} minutes.")

minutes_lived("27-10-1991")  #You have lived approximately 17916467 minutes.
minutes_lived("01-04-1988")  #You have lived approximately 19794227 minutes.
minutes_lived("05-06-2008")  #You have lived approximately 9181427 minutes.


#Exercise 7: Faker Module
import faker
users = []

def add_users():    #Inside the function, use a loop to generate the specified number of users.
    pass
