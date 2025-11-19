#DECORATORS  is way to DYNAMICALLY ADD some new behavior to some objects
# @ SYMBOL
#they can be STATIC --> NO SELF   @staticmethod
#     CLASS RELATED ---> SELF     @classmethod


import re                         #re stands for REGEX
import datetime 
class Person:
    def __init__(self, name, surname, birth_date):
        self.name = self.format_name(name)
        self.surname = self.format_name(surname)
        self.full_name = self.full_name()
        self.birth_date = birth_date                #age calculated with year

    @staticmethod                        # a STATIC METHOD is usually for internal formatting
    def format_name(name):
        name = name.strip().capitalize()       #it deletes spaces at start and end AND
        name = re.sub(r'[^a-zA-Z]', '', name)  #remove special chars and digits
        return name
    
    @staticmethod
    def parse_birth_date():
        pass

    @staticmethod 
    def full_name(name, surname):
        return f"{name}{surname}"

    @classmethod 
    def from_age(cls, name, surname, age):             #cls = class (Person, in this instance)
        current_year = datetime.datetime.today().year  # datetime.datetime. is fixed expression to which you append what needed
        birth_year = current_year - age
        birth_date = f'1-1-{birth_year}'
        return cls(name,surname,birth_date)            # cls = Person class
    
    @property 
    def full_name(self):
        self.full_name = f"{self.name},{self.surname}"  #TypeError: Person.full_name() takes 1 positional argument but 2 were given
        return self._full_name    
    @full_name.setter                                  #will allow me to print the method as if it was an attribute
    def full_name(self):
        pass
        #self.full_name = f"{self.name},{self.surname}"   

person1 = Person("JON","SNOWà","05-12-1980")
person2 = Person("Arya","Stark","03-07-2000")

print(person1.name, person1.surname)   #<<< Jon Snow
print(person2.name, person2.surname)   #<<< Arya Stark
print(datetime.datetime.today().year)  #<<<2025   #using print(datetime.datetime.today())>>>2025-11-18 10:57:34.794567

#creating an object with @classmethod

person3 = Person.from_age("Sansa", "stark", 30)
person4 = Person("daenerys","targaryen", 32)

print(person3.birth_date)    #<<< 1-1-1990
print(person4.birth_date)    #<<< 1-1-1988

#-----------------------------------------EXERCISE 
#create static method that formats name and surname as full_name
#create an internal attribute called "full_name" and do it with the "static method"
#print Daenerys' full name from person4 = Person("Daenerys","Targaryen", 32)

person3 = Person.from_age("Sansa", "stark", 30)
person4 = Person.from_age("daenerys", "targaryen", 30)
print(person4.full_name)



#DOUBLE UNDERSCORE "__" BEFORE A VALUE means protected (PRIVATE)


#CLASS ATTRIBUTE
#attribute that belongs to the CLASS and NOT TO EVERY INSTANCE
class Dog():
    dogs_king = "Bernie IV"                       #CLASS ATTRIBUTE

    # Initializer / Instance Attributes
    def __init__(self, name_of_the_dog):
        print("A new dog has been initialized!")
        print("His name is", name_of_the_dog)
        self.name = name_of_the_dog

    def bark(self):
        print(f"{self.name} barks bau!")

    def walk(self, number_of_meters):
        print(f"{self.name} walked {number_of_meters} meters.")

    def rename(self, new_name):
        self.name = new_name

my_dog = Dog("Rex")
                                            # A >>> A new dog has been initialized!
                                            # >>> His name is Rex
print("The king of the dogs is:", Dog.dogs_king)   #>>> The king of the dogs is: Bernie IV
                                                 # The dogs_king variable is now defined as “Bernie IV”, 
                                                 # we don’t need to have a Dog object to call this variable



# we can SAVE the NUMBER of DOGS ever created in a CLASS VARIABLE and INCREMENT it each time a dog is made 
# (in the __init__ function) ------------------------->

class Dog():
    number_of_dogs = 0                              #EMPTY class variable
    dogs_king = "Bernie IV"

    # Initializer / Instance Attributes
    def __init__(self, name_of_the_dog):
        print("A new dog has been initialized !")
        print("His name is", name_of_the_dog)
        self.name = name_of_the_dog
        Dog.number_of_dogs += 1                    # INCREMENT the NUMBER of dogs
       
    def bark(self):
        print(f"{self.name} barks ! WAF")

    def walk(self, number_of_meters):
        print(f"{self.name} walked {number_of_meters} meters")

    def rename(self, new_name):
        self.name = new_name

my_dog = Dog("Rex")              # >>> A new dog has been initialized ! His name is Rex
my_dog2 = Dog("Bernie V")        # >>> A new dog has been initialized ! His name is Bernie V
print(f"Currently, there are {Dog.number_of_dogs} dogs")     # >>> Currently, there are 2 dogs


#DUNDER METHODS (DOUBLE UNDERSCORE METHODS) --> ex. __init__, etc.
#they DO NOT NEED CALLING --> hence "MAGIC METHODS"

# 1) __str__

mylist = [1, 3, 5]
print(mylist.__str__())  #>>> [1, 3, 5] as a string

#2) __len__  ----->  return the length of the object

#3) __call__ 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __call__(self):
        print (f"Person: {self.name}, Age: {self.age}")

person1 = Person("Sarah", 25)
person1()                # class Person:
def __init__(self, name, age):
    self.name = name
    self.age = age

def __call__(self):
    print (f"Person: {self.name}, Age: {self.age}")

person1 = Person("Sarah", 25)     #>>> Person: Sarah, Age: 25

#3) __repr__
# is the representation of an object

class Person:
  def __init__(self, name, age):
      self.name = name
      self.age  = age

  def __repr__(self):
      return f"{self.__class__.__name__} : {self.name} {self.age}"

newPerson = Person('Sarah', 24)

print(newPerson)                      # >>> Person : Sarah 24


# 4 __add__

class Person:
  def __init__(self, name, lastName):
      self.name = name
      self.lastName = lastName

  def __repr__(self):
      return f"{self.__class__.__name__} : {self.name} {self.lastName}"

  def __add__(self, other):
      return Person(self.name, other.lastName)

father = Person('Daenerys', 'Snow')
mother = Person('Daenerys', 'Targaryen Stormborn MotherOfDragons BreakerOfChains')

# using the __add__() method
dragonChild = father + mother 

print(dragonChild)                       # Person : Daenerys Targaryen Stormborn MotherOfDragons BreakerOfChains
