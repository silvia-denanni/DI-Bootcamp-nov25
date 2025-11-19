# OOP COMPLEXITIES
# inheritance
# polymorphism
# encapsulation
# (abstraction) SELF LEARNING

#INHERITANCE: General Concept
#we can connect our classes by this principle

class Parent:               #PARENT CLASS
    def speak(self):        #METHOD FOR THIS CLASS
        print("Parent is speaking!")

class Child(Parent):        #CHILD CLASS REFERENCING THE PARENT (inside)
    def speak(self):
        print("Child is speaking!")

class Grandchild(Child):        #CHILD CLASS REFERENCING THE PARENT (inside)
    pass

child1 = Child()
child1.speak()              #>>> Child is speaking!

grandchild1 = Grandchild()
grandchild1.speak()         #>>> Child is speaking!

#INHERITANCE: ATTRIBUTES

class Animal:
    def __init__(self, name, family, legs):
        self.name = name
        self.family = family
        self.legs = legs
    
    def sleep(self):
        return f"{self.name} is sleeping"
    
class Dog(Animal):
    def __init__(self, name, family, legs, trained, age):
        super().__init__(name, family, legs)  #PUT what we wnt to inherit
        self.trained = trained
        self.age = age


class Cat(Animal):
    def __init__(self, name, family, legs, friendly, housecat):
        super().__init__(name, family, legs)   #taken from parent class
        self.friendly = friendly
        self.housecat = housecat



# dog1 = Dog("Ciro", "Canidae", 4) #we MUST put the ATTRIBUTES or the parent class!
# print(dog1.sleep())              
cat1 = Cat("Buffy","Felidae", 4, True, True)
print(cat1.friendly)     #True


# #MULTIPLE INHERITANCE  != HIERARCHICAL INHERITANCE   EX.

# class Alien:
#     def __init__(self, alienname, planet):
#         self.name = alienname
#         self.planet = planet

# class AlienDog(Alien, Dog): #THE ORDER GOES FROM 1 TO 2
#     def __init__(self, alienname, planet, ETC)
#     Alien.__init__(ETC)
#     Dog.__init__(ETC)

# alien_dog1 = AlienDog("Blrrb","Mars", "Laika","Canidae", 6 , True, 10)
# print(alien_dog1.planet)

# #EXCEPTIONS 

# Syntax:

# # try:
# #     PROBLEMATIC CODE     
# #     ADDITIONAL CODE  ------> WHEN WE HAVE AN ERROR, INSTEAD CRASHING AND IMPEDING PRINTING 
##                    -------->  REST OF THE CORRECT CODE FOLLOWING DOWN
# # except:
# #     EMERGENCY CODE

#EXAMPLE 

# print("this isn't a string)

# print("Will this run?")  #this won't be executed

# \                   #---> IT WILL NOT RUN


#TRY AND EXCEPT TO SOLVE THE PROBLEM
def age():
    user_age = input("How old are you?\n>>> ")     #PROBLEMATIC CODE
    
    try:                                           
        user_age = int(user_age)                   #ADDITIONAL CODE
        print("I AM AFTER USER_AGE")
    except:                                        
        print("Your age is not a real age")        #EMERGENCY CODE
        user_age = 0
    
    print(f"Next year, you will be {user_age+1} years old")

age()

#RUNNING THE CODE
# >>> How old are you?
# >>> 3weqf
# >>> Your age is not a real age
# >>> Next year, you will be 1 year old


#EXERCISE ON EXCEPTIONS:

# Given a list of numbers, write a function that returns the sum of every number. 
# BUT you can have a malicious string inside the list.

                                             #MY VERSION

my_list = [2,3,1,2,"four",42,1,5,3,"imanumber"]

def sum_list():                              # PROBLEMATIC CODE
    for x in my_list:
        if x is int                # SCORRETTO "is", CI VUOLE "isinstance"
              sum(my_list)

try:                                             
    my_list = [2,3,1,2,"four",42,1,5,3,"imanumber"]       #ADDITIONAL CODE
    items_to_bypass = "four","iamnumber"         
    for x, item in my_list:            # SCORRETTO, SPACCHETTA SOLO I TUPLE! MEGLIO "for x in my_list"
        clear_list = "".join([item for item in my_list if item != items_to_bypass])   #"".join NON NECESSARIO, OK LIST COMPREHENSION
    print(sum_list())            
    
except:                                     #EMERGENCY CODE
    print(f"This list {my_list} needs cleaning before summing the items inside of it") 
    # --------------->>> This list [2, 3, 1, 2, 'four', 42, 1, 5, 3, 'imanumber'] needs cleaning before summing 
    #                    the items inside of it
                                            

                                        #BETTER VERSION

my_list = [2,3,1,2,"four",42,1,5,3,"imanumber"]

def sum_list():                    # Only sum integers, skipping any items to bypass (if they were integers)
    cleaned_list
    cleaned_list = [x for x in my_list if isinstance(x, int)]
    return sum(cleaned_list)      #LEGGI SOTTO IMPORTANTEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE

#----return sum(cleaned_list) makes your function reusable, testable, and composable, while print(sum(cleaned_list)) 
#only displays the result and limits further use.-------------------------

try:
    result = sum_list()
    print(result)

except Exception as e:
    print(f"This list {my_list} needs cleaning before summing the items inside of it")  #>>>59