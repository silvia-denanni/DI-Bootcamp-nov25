#SEQUENCES are a CATEGORY of DATA STRUCTURES where ORDER MATTERS!
#1) LISTS: they need [] and you can put, strings, numbers (int and float), booleans, etc.
my_list =["apple", "banana", "cherry", 12, 1.09, True]
print(my_list)
print(my_list[5]) # You can access any element in your string by means of INDEXING []

new_list = ["apple", "banana", "cherry", [12,4,7]] #you can nest lists inside lists
print(new_list)
print(new_list[3]) #>>>[12, 4, 7]
print(new_list[3][1]) #>>>4

inside_list = new_list[3] #you can store an "inside list" inside a new variable -> "new_list" in this case
print(inside_list) #>>>[12, 4, 7] same as below
print(new_list[3]) ##>>>[12, 4, 7] same as above
print(inside_list[1]) #>>>4

grid = [[1,2,3], 
        [4,5,6],
        [7,8,9]
        ] #3 smaller lists inside a bigger list, I can make a game like checkers
print(grid[0][0]) #>> 1 --> I am getting the first element in the first sublist

#FUNCTIONS to modify lists, they are built-in in python
#--------------->LISTS, ONCE CHANGED, CANNOT BE ACCESSED ANYMORE IN THEIR OLD FORM!!!!!<----------

 #ADDING: .append()

my_list.append("this is the new last item")
print(my_list)

 #REMOVING: .remove()

my_list.remove("cherry") #this
print(my_list)  
                        #is the same as
my_list.remove(2) #this
print(my_list)  

 #.pop() --> REMOVES and RETURNS an element from the list, useful when you want to use the removed element.

my_list.pop(2) #>>> 'cherry' 

 #.extend() --> MERGING 2 LISTS TOGETHER

first_list = [1,2,3,4,5]
second_list = [6,7,8,9,10]

first_list.extend(second_list) #is the same 
print(first_list) #>>>[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(first_list + second_list) #is the same 
print(first_list) #>>>[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(sum(first_list)) #>>> 15
print(max(first_list))
print(min(first_list))

print(max([[1,2,3], 
        [4,5,6],
        [7,8,9]])) #>>>[7, 8, 9]

#-----------------LIST SLICING-----------------
vinted_cart = ["boots","dress", "belt", "ring"]
print(vinted_cart[0:2]) # ['boots', 'dress']

vinted_cart = ["boots", "cat tree", "dress"]
vinted_cart[0] = "sandals"
new_cart = vinted_cart
new_cart = vinted_cart[0] = "cat toy"
print(new_cart) # cat toy
print(vinted_cart) # ['cat toy', 'cat tree', 'dress']

#2) TUPLES are immutable!

tup = (1,2,3,4,"happy bday!")
print(tup) # --> (1, 2, 3, 4, 'happy bday!')

tup[0] = 42 # --- ERROR  ---> IMMUTABLEEEEEEEEEEEEEE

#TUPLES can be separated into individaul items

tup = (1,2,3,4,5)
a,b,c,d,e = tup
print(a) #1
print(b) #2
print(c) #3
print(d) #4
print(e) #5

a,b = tup # --- ERROR too many values to unpack (expected 2) ---

a, b*= tup # you can assign anyting else with a *, noe it will work
print(a) #1
print(b) #2


#SETS: UNORDERED, NO INDEX! They are NOT SEQUENCES and they print UNIQUE VALUES, no repetitions

# --------------------To create a set, you can use curly braces {}
lista_mia = {1,2,2,5,6}
print(lista_mia)  # {1, 2, 5, 6} NO DUPLICATES in sets!

# Using the set() function with an iterable (such as a LIST):
my_set = set([1, 2, 2, 3, 4])
print(my_set)  # Output: {1, 2, 3, 4} NO DUPLICATES in sets!

#BASIC OPERATIONS ON SETS
miao = {1, 2, 3}
bau = {3, 4, 5}

# Union: all unique elements from both sets
print(miao.union(bau)) # Output: {1, 2, 3, 4, 5}

# Intersection: elements common to both sets
print(miao.intersection(bau)) # Output: {3}

# Difference: elements in a but not in b
print(miao.difference(bau))  # Output: {1, 2}

# Add an element
miao.add(6)
print(miao) # Output: {1, 2, 3, 6}

# Remove an element
miao.remove(2)
print(miao)  # Output: {1, 3, 6}

#LOOPS 
 #1)FOR LOOP
#SYNTAX
#FOR <variable_name> in <sequence_name>:
    #..
                                             # PRACTICAL SYNTAX EXAMPLE
number_list =[12,34,56,75,99]
for number in number_list: #This tells Python to retrieve the first value from number_list and
                           #store it in the variable "number"

                                             # REAL EXAMPLES
number_list= [12,34,56,75,99]

for number in number_list:
        print(number_list) #>>> [12, 34, 56, 75, 91]

for item in number_list:
        if item > 200:
                print("Big numebr is ", item)
        else:
                print("Small number is ",item) # Small number is  12
# Small number is  34
# Small number is  56
# Small number is  75
# Small number is  99



number_list =[12,34,56,75,99]
my_sum = 0

for item in number_list:
     my_sum = my_sum + item
     print("Current sum:", my_sum)

print("Final sum:", my_sum) #>>>Current sum: 12                            
                            # Current sum: 46
                            # Current sum: 102
                            # Current sum: 177
                            # Current sum: 276
                            # Final sum: 276




 #2)WHILE LOOP: runs as long as a certain condition is TRUE
                                            # SYNTAX OF A WHILE LOOP -->
                                  # while some_condition:
                                     # do something
                                  #else:
                                     # do another thing


                                             # REAL EXAMPLES WHILE LOOPS
list = [1,6,7,9,4,3]

j = 0
while j < len(list):
        print(list[j])
        j = j + 1 #!!!!!!!!! this line is VERY IMPORTANT to change the value you want to assign to the variable !!!!!!!!!!!!


# password = "secret"
# guess = input("What is the password? ")
# while guess != password:
#         print("Incorrect password! Try again!")
#         guess = input("What is the password? ")     #guess = "orange" ---------------WITHOUT IT IT WOULD GO ON FOREVER------------

# print("Correct password!")      #REVIEWWWWWWWWWWWWWWWWWWwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww


#---------------CAREFUL WITH INFINITE LOOPS!---------------------------
# while 1 == 1:
#     print("Looping...")
                                                       #FOREVERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
#---------------YOU NEED TO USE "break"

list = [1,6,7,9,4,3,10]

for item in list:
        if item > 9:
                print("big number found!")
        break         # HERE WE ARE BREAKING OUT of a loop entirely WITHOUT EXECUTING the rest of its code (NO ELSE!)
else:
        print(f"current number is: {list}") # big number found! 
        


#--------------------"continue" TO RETURN TO THE BEGINNING OF THE LOOP
#

i = 0
while i < 10:
        i += 1
        if i % 2 ==0:
                continue  #REVIEW
        print(i)  #1
# 3
# 5
# 7
# 9


#ENUMERATE
for char in enumerate("Hellooo"):
        print(char)
# (0, 'H')
# (1, 'e')
# (2, 'l')
# (3, 'l')
# (4, 'o')
# (5, 'o')
# (6, 'o')