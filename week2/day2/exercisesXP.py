#Exercise 1: Pets
#Use the provided Pets and Cat classes to create a Siamese breed, instantiate cat objects, and use the Pets class to manage them.
#See the example below, before diving in.
# Step 1: Create the Siamese Class
# Step 2: Create a List of Cat Instances
# Step 3: Create a Pets Instance
# Step 4: Take Cats for a Walk

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk)

class Cat():
    def __init__(self, name, age, friendly):
        self.name = name
        self.age = age
        self.friendly = friendly

    def walk(self):
        return f"{self.name} is just walking around"

class Siamese(Cat):
    def __init__(self, name, age, friendly, vocal, eye_color, fur_color):
        super().__init__(name, age, friendly)
        self.vocal = vocal
        self.eye_color = eye_color
        self.fur_color = fur_color
    
    def walk(self):
        def walk(self):
            return f"{self.name} is just walking around"

all_cats = [Cat("Cordelia",15, False),
            Cat("Tara",9, True),
            Siamese("Xander",13, True, True, "blue", "colorpoint"),
            Siamese("Buffy",15, True, True, "blue", "colorpoint")]

sara_pets = Pets(all_cats)

print(sara_pets.walk())

#2) Exercise 2: Dogs

# Step 1: Create the Dog Class
# Step 2: Create Dog Instances
# Step 3: Test Dog Methods
# Call the bark(), run_speed(), and fight() methods on the dog instances to test their functionality.

class Dog():
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    
    def bark(self):
        print (f"{self.name} is barking")
    
    def run_speed(self):
        return self.weight / self.age * 10 
    
    def fight(self, other_dog):
        my_power = self.run_speed() * self.weight
        other_power = other_dog.run_speed() * other_dog.weight
        if my_power > other_power:
            f"{self.name} won the fight against {other_dog.name}!"
        elif my_power < other_power:
            f"{other_dog.name} won the fight against {self.name}!"
        else:
            f"It is a tie between {other_dog.name} and {self.name}!"


dog1 = Dog("Ciro", 3, 15)                     #we MUST put the ATTRIBUTES or the parent class!
dog2 = Dog("Rosetta", 10, 3) 
dog3 = Dog("Haku", 7, 8,5) 

print(dog1.bark())
print(dog2.bark())

print(dog2.run_speed())
print(dog1.fight(dog2))
print(dog1.fight(dog3))

print(f"{dog1.name} run speed is: {dog1.run_speed():.2f}")
print(f"{dog2.name} run speed is: {dog2.run_speed():.2f}")
print(f"{dog3.name} run speed is: {dog3.run_speed():.2f}")


#Exercise 3: Dogs Domesticated
# trained means that the dog is trained to do some tricks.
import dogClass
import random

class PetDog(dogClass):
    def __init__(self, name, age, weight, trained = False):
        super().__init__(name, age, weight)
        self.trained = trained

    def train(self):
        self.bark()
        self.trained = True

    def play(self, *args):
        dog_names = [self.name] + [dog.name for dog in args] #*args on this method is a list of dog instances.
        print(f"{', '.join(dog_names)} all play together.")

    def do_trick(self):
        tricks = ["does a barrel roll", 
                  "stands on his back legs", 
                  "shakes your hand", "plays dead"]
        if self.trained == True:
            trick = random.choice(tricks)  # Choose a random index from it each time the method is called.

            print(f"{self.name} {trick}")
        else:
            print(f"{self.name} is not trained yet and cannot do tricks.")
    
# Create instances of the PetDog class and test the train(), play(*args), and do_a_trick() methods.

dog1 = PetDog("Ciro", 4, 15)
dog2 = PetDog("Rosetta", 9, 8)
dog3 = PetDog()

dog3.train()
dog2.play(dog1, dog3)
dog1.do_trick()
dog3.do_trick()


# Exercise 4: Family and Person Classes

# Step 1: Create the Person Class

# Define a Person class with the following attributes:
# first_name
# age
# last_name (string, should be initialized as an empty string)
# Add a method called is_18():
# It should return True if the person is 18 or older, otherwise False.


# Step 2: Create the Family Class

# Define a Family class with:
# A last_name attribute
# A members list that will store Person objects (should be initialized as an empty list)


# Add a method called born(first_name, age):
# It should create a new Person object with the given first name and age.
# It should assign the family’s last name to the person.
# It should add this new person to the members list.


# Add a method called check_majority(first_name):
# It should search the members list for a person with that first_name.
# If the person exists, call their is_18() method.
# If the person is over 18, print:
# "You are over 18, your parents Jane and John accept that you will go out with your friends"
# Otherwise, print:
# "Sorry, you are not allowed to go out with your friends."


# Add a method called family_presentation():
# It should print the family’s last name.
# Then, it should print each family member’s first name and age.


# Expected Behavior:

# Once implemented, your program should allow you to:

# Create a family with a last name.
# Add members to the family using the born() method.
# Use check_majority() to see if someone is allowed to go out.
# Display family information with family_presentation().
# Don’t forget to test your classes by creating an instance of Family, adding members, 
# and calling each method to see the expected output.