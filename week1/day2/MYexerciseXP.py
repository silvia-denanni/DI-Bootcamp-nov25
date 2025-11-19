#1 Create a set called my_fav_numbers and populate it with your favorite numbers.
# Add two new numbers to the set.
# Remove the last number you added to the set.
# Create another set called friend_fav_numbers and populate it with your friend’s favorite numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to create a new set called our_fav_numbers.
# Note: Sets are unordered collections, so ensure no duplicate numbers are added.

my_fav_numbers = {1,3,5}
print(my_fav_numbers)
my_fav_numbers.add(11)
my_fav_numbers.add(13)
my_fav_numbers.remove(13)
print(my_fav_numbers)

my_friend_numbers = {2,4,6}
our_numbers = my_fav_numbers | my_friend_numbers
print(our_numbers)

#ALTERNATIVE 1

# my_friend_numbers = {2,4,6}
# our_numbers = my_fav_numbers.union(my_friend_numbers)
# print(our_numbers)

#ALTERNATIVE 2

# my_friend_numbers = {2,4,6}
# our_numbers = my_fav_numbers.update(my_friend_numbers)
# print(my_fav_numbers)



#2 Given a tuple of integers, try to add more integers to the tuple--> Tuples are IMMUTABLE, they cannot be changed after creation.

#3 
# You have a list: basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# Remove "Banana" from the list.
# Remove "Blueberries" from the list.
# Add "Kiwi" to the end of the list.
# Add "Apples" to the beginning of the list.
# Count how many times "Apples" appear in the list.
# Empty the list.
# Print the final state of the list.

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# basket.remove("Banana")
# print(basket)

# basket.remove("Blueberries")
# print(basket)

# basket.append("kiwi")
# print(basket)

# basket.insert(0,"Apples")
# print(basket)

# count_apples = basket.count("Apples")
# print(count_apples)

# basket.clear()
# print(basket)

#4) Create a list containing the following sequence of mixed types: floats and integers:
# 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5.
# Avoid hard-coding each number manually.
# Think: Can you generate this sequence using a loop or another method?

sequence = []
start = 1,5
end = 5
step = 0.5

current = start
while current <= end:
    if current.is_integer():
        sequence.append(int(sequence)) # sequence.append(int(current)) converts values like 2.0 to 2 before storing.

    else:
        sequence.append(current)
    current += step #moves to the next value for the next loop run
    
print(sequence)

