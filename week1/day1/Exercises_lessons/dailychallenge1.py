import random   # is a convention to start like that if u want to work with this module or others

user_string =(input("Please enter a 10 character long string: "))
if len(user_string) < 10:
    print("Please enter a longer string.")
elif len(user_string) > 10:
    print("Please enter a shorter string.")
else: 
    print(f"Your string is such a 10! The first character is {user_string[0]} and the last character is {user_string[9]}")
for i in range(1, len(user_string) + 1): #RANGE FUNCTION: range(len(user_string) + 1) --> it becomes 11 (10 +1). 
#Then, the range(1, 11) creates a sequence of counting numbers starting at 1 and going up to, but not including, 11.
#LOOP: for i in --> do the following step n times, and in each step, let the variable i be the next number in the
# count (1, 2, 3, etc.)
    print(user_string[:i]) #STRING SLICING: user_string[:i] --> user_string[start : end]; since 0 is not mandatory, i only
# indicates the end position

random_list = random.sample(user_string,len(user_string))
print(random.sample(user_string,len(user_string))) #since strings are immutable and stay in memory, if you want to act on
# them you can use functions (like here import.random ....)

#join takes a list of random elements and transforms it into a string

jumble_string = "".join(random_list)
print(jumble_string)

# ALTERNATIVE CODE BEFORE BONUS

# user_string =(input("Please enter a 10 character long string: "))
# if len(user_string) < 10:
#     print("Please enter a longer string.")
#     return  #better to add
# elif len(user_string) > 10:
#     print("Please enter a shorter string.")
#     return  #better to add
# else: 
#    print("Perfect string!")
#    print(f"First character:{user_string[0]}")
#    print(f"Last character:{user_string[-1]}")

# constructed_string = ""
# for char in user_string:
#     constructed_string += char
#     print(constructed_string)

