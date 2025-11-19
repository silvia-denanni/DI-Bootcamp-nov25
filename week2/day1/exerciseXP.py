# Exercise 1: Cats
# Step 1: Create Cat Objects
# # Use the Cat class to create three cat objects with different names and ages.

# Step 2: Create a Function to Find the Oldest Cat
# # Create a function that takes the three cat objects as input.
# # Inside the function, compare the ages of the cats to find the oldest one.
# # Return the oldest cat object.

# Step 3: Print the Oldest Cat’s Details
# # Call the function to get the oldest cat.
# # Print a formatted string: “The oldest cat is <cat_name>, and is <cat_age> years old.”
# # Replace <cat_name> and <cat_age> with the oldest cat’s name and age.

class Cat():
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

cat1 = Cat("Tuli", 11)
cat2 = Cat("Buffy", 4)
cat3 = Cat("Turli", 1)

def find_oldest_cat (cat1, cat2, cat3):
    if cat1.age > cat2.age:
        return cat1
    elif cat2.age > cat1.age:
        return cat2
    else:
        return cat3

oldest_feline = find_oldest_cat(cat1, cat2, cat3)
print(f"The oldest cat is {oldest_feline.name} who is {oldest_feline.age}!")
       

## Exercise 2: Dogs
##Step 1: Create the Dog Class

# # In the __init__ method, take name and height as parameters and create corresponding attributes.
# # Create a bark() method that prints “<dog_name> goes woof!”.
# # Create a jump() method that prints “<dog_name> jumps <x> cm high!”, where x is height * 2.

##Step 2: Create Dog Objects

# # Create davids_dog and sarahs_dog objects with their respective names and heights.

##Step 3: Print Dog Details and Call Methods

# Print the name and height of each dog.
# Call the bark() and jump() methods for each dog.


##Step 4: Compare Dog Sizes

class Dog():
    def __init__(self, dog_name, dog_height):
        self.name = dog_name
        self.height = dog_height
    
    def bark(self):
        print(f"{self.name} goes bau!")

    def jump(self):
        jump_height = self.height * 2
        return jump_height
    
    def compare_dog_size(self):
        if self.height < 20:
            return (f"{self.name} is the smaller dog.")
        else:
            print(f"{self.name} is the bigger dog.")
            return self.height      

davids_dog = Dog("Ciro", 20)
sarahs_dog = Dog("Rosetta", 10)

davids_dog.bark()
sarahs_dog.bark()

print(davids_dog.jump())
print(sarahs_dog.jump())

print(davids_dog.compare_dog_size())
print(sarahs_dog.compare_dog_size())
        
# # Exercise 3 : Who’s the song producer?
# # Step 1: Create the Song Class    
class Song():
    def __init__(self, name, lyrics):
        self.name = name
        self.lyrics = lyrics

    def sing_me_a_song(self):
         for line in self.lyrics:  #For each element in the list self.lyrics, assign it temporarily to the variable line.
            print(line)
        
stairway = Song("Stairway to Heaven", [
    "There\'s a lady who\'s sure",
    "all that glitters is gold",
    "and she\'s buying a stairway to heaven"
    ])

stairway.sing_me_a_song()

# # Exercise 4 : Afternoon at the Zoo
# # Step 1: Define the Zoo Class
# # Create a class called Zoo.

# # 2. Implement the __init__() method:

# # It takes a string parameter zoo_name, representing the name of the zoo.
# # Initialize an empty list called animals to keep track of animal names.

# # 3. Add a method add_animal(new_animal):

# # This method adds a new animal to the animals list.
# # Do not add the animal if it is already in the list.

# # 4. Add a method get_animals():
# # This method prints all animals currently in the zoo.

# # 5. Add a method sell_animal(animal_sold):
# # This method checks if a specified animal exists on the animals list and if so, remove from it.

# # 6. Add a method sort_animals():
# # This method sorts the animals alphabetically.
# # It also groups them by the first letter of their name.
# # The result should be a dictionary where:
# # Each key is a letter.
# # Each value is a list of animals that start with that letter.

class Zoo():
    def __init__(self,zoo_name):
        self.name = zoo_name
        self.animals = [] # empty list to keep track of animal
    
    # def add_animal(self, new_animal):
    #     if new_animal not in self.animals:
    #         self.animals.append(new_animal)
    #     else:
    #         print("This animal already is in the zoo.")

    def add_animal (self, *new_animal):   #KWARGS ALWAYS CREATE A DICTIONARY
        if new_animal:
            for each_animal in self.animals:
                if each_animal not in self.animals:
                    self.animals.append(new_animal)
                else:
                    print("{each_animal} exist in the zoo")
        print("," .join(self.animals))


    def get_animal(self):
        if not self.animals:
            print("There are no animals in the zoo")
        else:
            print("," .join(self.animals))              #REVIEW THE JOIN METHOD

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f"{animal_sold} was sold.")

    def sort_animals(self):
        sorted_animals = sorted(self.animals) #creates a new list of animals sorted in alphabetical order
        grouped_animals = {} # empty dictionary to hold groups of animal

        for animal in sorted_animals: # goes through each sorted animal one at a time
            first_letter = animal[0].upper() #  the first letter will be used to group animals
            if first_letter not in grouped_animals:
                grouped_animals[first_letter] = [] # create new list if dictionary key "letter" doesn't exist
        grouped_animals[first_letter].append(animal) # adds the current animal to the group corresponding to its first letter

        return grouped_animals           

    def get_groups(self):
        groups = self.sort_animals() # calls the "sort_animals" function to get the grouped dictionary
        for letter in sorted(groups.keys()): #goes through the letters (keys) in alphabetical order.
            print(f"{letter}:")
            for animal in groups[letter]: #to print each animal individually.
                print(f"{animal}:")
        return groups


crazy_zoo = Zoo("Crazy Zoo")
# # print(crazy_zoo.name)
# crazy_zoo.add_animal("Giraffe")
# print(crazy_zoo.animals)
# crazy_zoo.add_animal("Gerbil")
# print(crazy_zoo.animals)
# crazy_zoo.add_animal("Porcupine")
# print(crazy_zoo.animals)
# crazy_zoo.add_animal("Baboon")
# print(crazy_zoo.animals)
# crazy_zoo.get_animal()
# crazy_zoo.sort_animals
# print(crazy_zoo.sort_animals())
crazy_zoo.add_animal("Monkey", "Meerkat", "Mermaid")