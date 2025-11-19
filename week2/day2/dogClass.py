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