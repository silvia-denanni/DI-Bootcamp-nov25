# #1)
# class Animal():
#     def __init__(self, type, age, sound, number_legs):
#         self.type = type
#         self.age = age
#         self.sound = sound
#         self.number_legs = number_legs

#     def make_sound(self):
#         print(f"I am an animal, and I love saying {self.sound}")

# class Dog(Animal):
#     def fetch_ball(self):
#         print("I am a dog and I love to fetch balls")

# rex= Dog("dog", 4, "wouaf", 4)
# print('This animal is a:', rex.type)   #This animal is a dog

# ciro = Dog("dog", 3, "bau", 4)
# print("This animal is a:", ciro.type)   #This animal is a dog

# rosetta = Dog("dog", 9, "nothing", 4)
# print("This animal is a", rosetta.type)  #This animal is a dog
# print("This dog is ",rosetta.age, "years old")  #This dog is 9 years old

# ciro.make_sound()      #I am an animal, and I love saying wouaf
# rosetta.fetch_ball()   #I am a dog and I love to fetch balls



# #2) 
# class Circle:
#     def __init__(self, diameter):
#       self.diameter = diameter

#     def grow(self, factor=2):
#         """grows the circle's diameter by factor"""
#         self.diameter = self.diameter * factor

# class NewCircle(Circle):
#     def grow(self, factor=2):
#         """grows the area by factor..."""
#         self.diameter = (self.diameter * factor * 2)

# nc = NewCircle(1)
# print(nc.diameter)         #1

# nc.grow()

# print(nc.diameter)         #4


# # Overriding Parent Methods 
# # CHILD CLASSES OVERRIDE or EXTEND the functionality of PARENT ones: will have both INHERITED + OWN


# # Returning Parent OVERRIDDEN methods:------------------- super() Function -------------------------
# class Animal():
#     def __init__(self, type, number_legs, sound):
#         self.type = type
#         self.number_legs = number_legs
#         self.sound = sound

# class Dog(Animal):
#     def __init__(self, type, number_legs, sound, fetch_ball):              #OWN
#         super().__init__(type, number_legs, sound)                         #PARENT
        
#         self.fetch_ball = fetch_ball

# rex = Dog ("dog", 4, "wouaf", True)
# print("Does this dog fetchs balls?", rex.fetch_ball)        # Does this dog fetchs balls? True

#EXERCISE --------------------- SPOT THE DIFFERENCE

# #1
# class A(B):
#     def __init__(self, *args, **kwargs)      
#         B.__init__(self, *args, **kwargs)       #HERE YOU NEED TO PUT "self" FIRST BECAUSE THERE IS NO super()
#         pass
# #2
# class A(B):
#     def __init__(self, *args, **kwargs)
#         super().__init__(*args, **kwargs)       #HERE you do not need to put "self", it is alreday included in super()
#         pass

#EXERCISE ------------------------ Door class initiation
# We have a class called Door that has an attribute of is_opened declared when an instance is initiated.


class Door():
    def __init__(self, is_open):
        self.is_open = is_open        #ATTRIBUTE

class BlockedDoor():
    def __init_subclass__(cls, ):
        pass

door1 = Door(True)
print(door1.is_open)    #>>>True------------------- #TO BE CALLED WITH NO PARENTHESES, IT IS NOT A METHOD!!!


#EXERCISE ------------------------ Door class creation with EXCEPTIONS
# We have a class called Door that has an attribute of is_opened declared when an instance is initiated.
# We can create a class called BlockedDoor that inherits from the base class Door.
# We just override the parent class's functions of open_door() and close_door() with our own BlockedDoor 
#      version of those functions, which simply raises an Error that a blocked door cannot be opened or closed.


class Door():                        #BASE CLASS
    def __init__(self, is_open):
        self.is_open = is_open        #ATTRIBUTE

    def open_door(self):             #METHOD 1
        self.is_open = True
        print("The door was opened")

    def close_door(self):            #METHOD 2
        self.is_closed = False
        print("The door was closed")

class BlockedDoor(Door):  #inherits ATTRIBUTES from the base class "DOOR"
    def open_door(self):                 #METHOD OVERRIDES PARENT
        raise Exception("A blocked door cannot be opened.") #raises an Error that a blocked door cannot be opened 
    def close_door(self):                #METHOD OVERRIDES PARENT
        raise Exception("A blocked door cannot be closed.") #raises an Error that a blocked door cannot be closed
    
door1 = Door(True)
door1.open_door()   #The door was opened

door1 = Door(False)
door1.close_door()  #The door was closed

blocked1 = BlockedDoor(False)
try:
    blocked1.open_door()
except Exception as e:
    print(e)   # Exception: A blocked door cannot be opened.

# blocked2 = BlockedDoor(True)
# try:
#     blocked2.close_door()  
# except Exception as e: 
#      print(e)  # Exception: A blocked door cannot be closed.



#     def __init__(self, name): # When you add __init__(), the child class will no longer inherit the parent's __init__(
#         super().__init__()   #you do not have to use the name of the parent element
        