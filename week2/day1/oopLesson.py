#DESCRIBING AN OBJECT: A SERIES OF ATTRIBUTES THAT DEFINE THAT SPECIFIC "CLASS", THAT CAN BE DECLINED 
#IN MANY DIFFERENT INSTANCES
#class "bottle" has many ATTRIBUTES, KINDA LIKE A DICTIONARY:
#{"material": "metal", "usage": "store liquids", "color": "white"} 

#OOP HOW TO CREATE A CLASS OF OBJECTS IN PYTHON
class Dog:           #"class" KEYWORD; the name is written in singular, CamelCase 
    def __init__(self, name, color, breed, age, is_trained = True): # "def__init__ is" the class builder function; "self" is to
        self.name = name                                    #setting up all of the ATTRIBUTES in order to create
        self.color = color                                  #the dog object
        self.breed = breed
        self.age = age
        self.is_trained = True

#----------------------------------------------- #creating METHODS (FUNCTIONS)  to determine actions

    def bark(self):                      
        print(f"{self.name} goes woof woof")

    def run(self):
        if int(self.age) > 5:
            print(f"{self.name} prefers to walk")
        else:
            print(f"{self.name} is running")
    
    def walk(self, person):
        print(f"{person} is walking {self.name}")

    def rename(self, new_name):
        self.name = new_name
        return self                                #BEST PRACTIVE INSTEAD OF print()

# HOW TO CREATE AN OBJECT (or INSTANCE) FROM A SPECIFIC CLASS   #>>> print(class(dog1)) ----->  <class '__main__.DogBreed'>

dog1 = Dog("Rex","black","german shepherd","8","True")   #dog1 --> first object (instance) of the class "DogBreed"
print(dog1.name)                                           
print(dog1.age)
print(dog1.is_trained)                                  #this is how you can access the attributed of the obj/instance
print(dog1.__dict__)

dog1.service_dog = True               #how to add an attribute to object/instance dog1 in class "Dog"
print(dog1.service_dog)     #>>> True          


#EXERCISE: -----------------------------------------CREATE YOUR OBJECT (dog2) originating from the "Dog" class
dog2 = Dog("Ciro", "orange and white", "Corgi", "3", "True")
print(dog2.name)
print(dog2.color)
print(dog2.breed)
print(dog2.age)
print(dog2.is_trained)
print(dog2.__dict__)     #>>> {'name': 'Ciro', 'color': 'orange and white', 'breed': 'Corgi', 'age': '3', 'is_trained': 'True'}

#CALL THE METHOD
dog1.bark()
dog2.bark()
dog1.run()
dog2.run()
dog2.walk("Michela")
dog1.rename("Haku")
print(dog1.name)


#------------------------------------------------------#EXERCISES
#1)

class Person():
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def show_details(self):
    print(f"Hello my name is {self.name} and I am {self.age} years old")

first_person = Person("John", 36)
first_person.show_details()    #>>> Hello my name is John and I am 36 years old

#2)
 
                # == Computer.description(dell_computer, "Mark")


#3)               ------------------- EXERCISE  Create a character

class PlayerCharacter:
    membership = True               #Class Object Attribute: it is ALWAYS VALID for every instance of the class
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def shout(self):
        print(f"My name is {self.name}!")
    
    def greeting(self, greeting):
        print(f"{greeting}!")

player1 = PlayerCharacter("Elettra", 17)

player1.shout()                # >>> My name is Elettra!
player1.greeting("Hello!")     # >>> Hello!

#4) ----------------------------------EXERCISE : CALCULATOR

class calculator():
    def add(x,y):
        answer = (x + y)
        print(answer)
    
    def subtract(x,y):
        answer = (x - y)
        print(answer)

    def multiply(x,y):
        answer = (x*y)
        print(answer)
    
    def divide(x,y):
        answer = (x/y)
        print(answer)

calculator.add(5,7)                #12
calculator.multiply(17,19)         #323

# -----------------------------EXERCISE: CREATE BankAccount class with 3 features:
# -holder = name, last_name, 
# -number = random
# -balance = 50.00

#EXERCISE ----------------------------------------class BankAccount:

class BankAccount():

    def __init__(self, owner, account_id, balance =50.00):
        self.owner = owner
        self.account_id = account_id
        self.balance = balance
        
    def view_balance(self):
        report = f'''account holder: {self.owner}
         account number: {self.account_id} 
         balance :${self.balance:.2f}'''
        print(report)

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount")
        else:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal impossible, the amount is not positive.")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"You withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")

account1 = BankAccount("Daniela", 123456)
account1.view_balance()
account1.deposit(100)
account1.withdraw(30)

#TO IMPORT CURRENT DATE

import datetime                   #at the very beginning
datetime.datetime.now()           #inside the actual code


#----------------------------------EXERCISE: CREATE BankAccount ALTERNATE VERSION
class BankAccount:

    def __init__(self, account_number, balance=0):  #we start at 0 
        self.account_number = account_number
        self.balance = balance
        self.transactions = []           #empty list to fill up

    def view_balance(self):
        self.transactions.append("View Balance: ")
        print(f"Balance for account {self.account_number}: {self.balance}")

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid: negative amount.")
        elif amount < 100:
            print("Minimum deposit is 100")
        else:
            self.balance += amount
            self.transactions.append(f"Deposit: {amount}.")
            print(f"Deposit Succcessful! ${amount} added to the balance.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds, sorry.")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdraw: {amount}")
            print("Withdrawal approved!")
            return amount

    def view_transactions(self):
        print("Transactions:")
        print("-------------")
        for transaction in self.transactions:
            print(transaction)

account1 = BankAccount(123456, 0)
account1.view_balance() # Balance for account 123456: 0
account1.deposit(500)   # Deposit Succcessful! $500 added to the balance.
account1.view_balance()  # Balance for account 123456: 500
account1.withdraw(130000) # Insufficient funds, sorry.
account1.withdraw(13000)  # Insufficient funds, sorry.
account1.withdraw(1300)   # Insufficient funds, sorry.
account1.withdraw(130)    # Withdrawal approved!
account1.view_transactions() #Transactions:
                             #-------------
                             #View Balance:
                             #Deposit: 500.
                             #View Balance:
                             #Withdraw: 130
account1.view_balance()      #Balance for account 123456: 370

