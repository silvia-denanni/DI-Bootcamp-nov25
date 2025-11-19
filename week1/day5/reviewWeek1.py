#DAY2 LISTS -- MUTABLE, ORDERED SEQUENCE
friends = ["Monica", "Ross", "Rachel", "Joey", "Chandler", "Phoebe"]

#LIST SLICING (CAN BE DONE ALSO TO STRINGS)
print(friends[2])
print(friends[2:5]) #from 2 to 5

#LIST METHODS
                                    #THERE IS NO REPLACE FOR lists: ONLY .insert AND THEN .remove
#ADDING, REPLACING, REMOVING
friends.append("Silvia")   #AT THE END
friends.insert(2,"Silvia")  #IN THE POSITION SPECIFIES
friends.remove("Monica")        #WE ARE PERFORMING A REPLACEMENT HERE
print(friends)

del friends[2]

#ORDERING  .sort VS .sorted
friends.sort()
print(friends)          #['Chandler', 'Joey', 'Monica', 'Phoebe', 'Rachel', 'Ross']

#SPLITTING .split  __IT CREATES A LIST AS AN OUTPUT
user_info = input("Enter your name and age separated by a comma: ".split(","))
print(user_info)               #SILVIA, 35

#JOIN   .join

# students = input("Enter student names: ").split()
# print(f"The new students are: {','".join(students)}")         


#MAP map() SYNTAX 

#----------------------------------                 map(action,[list])

                     #EXAMPLE
def multiply_by_2(li):
    new_list = []                         # all of this
    for item in li:                       # becomes unnecessary
        new_list.append(item*2)           # with map()
    return new_list    
print(multiply_by_2([1,2,3]))             #>>>[2, 4, 6]


#------------------------------- map() SIMPLIFIES FUNCTIONS WE CREATED -----------------------------------------------------
def multiply_by_2(item):
    return item*2

print(list(map(multiply_by_2, [1,2,3])))  #>>>[2, 4, 6]
                                    #map() runs the function "multiply_by_2" for us and loops through the items
                                    #inside [] and it returns a new "map" object, that we convert into a list (list())

#-------------------------------------------- ANOTHER map() example

my_list = [3,6,7]                 #we are "mapping" over each item, always the same, they stay
def multiply_by_2(item):
    return item*2

print(list(map(multiply_by_2,(my_list)))) #>>>[6, 12, 14]  
                    
                              #output is another list based on the original one ----------------------------------

#FILTER filter() SYNTAX
#------------------------------filter(action, list)

my_list = [3,6,7]      #this original list stays           
def multiply_by_2(item):
    return item*2

def is_odd(item):
    return item % 2 != 0

print(list(filter(is_odd, my_list)))    #>>>[3, 7]     it gives me back only the ODD values in the new list created
                                                      #on the basis of our old one 


#ZIP zip() --> it "zips" together 2 or several iterables (lists, tuples) giving as an output a TUPLE LIST
#                                   SYNTAX             zip(iterable, iterable)

my_list = [3,6,7]      #this original list stays           
def multiply_by_2(item):
    return item*2
pass
#print(my_list)

def is_odd(item):
    return item % 2 != 0

#print(list(filter(is_odd, my_list)))
pass

your_list = [2,5,8]
def is_even(item):
    return item % 2 == 0

print(list(zip(my_list, your_list)))        #[(3, 2), (6, 5), (7, 8)] 
                                     #zip(my_list, your_list) pairs elements from my_list and your_list by their 
                                     # positions:
#                                       First pair: (3, 2)
#                                       Second pair: (6, 5)
#                                       Third pair: (7, 8)
#                                       list() converts the zip object into a list of tuples.



# REDUCE (to be imported):  it takes your LISR and REDUCES it to ONE VALUE by applying a function repeatedly

#SYNTAX                     from functools import reduce
#                           "reduce"("lambda" X,Y: expression) 

#                           reduce needs a function --(lambda)-- that takes 2 arguments in the expression 
#                                --> (X does sothg with Y)
#                           1)The first argument in the expression is the accumulated value so far 
#                                --> X or ACC
#                           2)The second argument is the next item from the list 
#                                --> Y or ITEM


#               ........>    the LAMBDA FUNCTION is written inline, used only ONCE    ......>


#               ........>             NO DEF NECESSARY TO CREATE A FUNCTION"        <.........


                            # EXAMPLE: ADDING NUMBERS

numbers = [1, 2, 3, 4, 5]

from functools import reduce
result = reduce(lambda x, y: x + y, numbers) #LAMBDA creates a quick, anonymous function (NO NEED FOR DEF!!!!!!!!!)
#-----------------------------------------------> take two numbers x and y, and give back their SUM

print(result)           # >>> 15

                        #  1) it adds 1 and 2 → 3
                        #  2) it adds 3 (the result) and 3 → 6
                        #  3) it adds 6 and 4 → 10
                        #  4) it adds 10 and 5 → 15 final result



                       # EXAMPLE: MULTIPLYING NUMBERS

numbers = [2,3,4,5,6]

from functools import reduce
result = reduce(lambda x, y: x*y, numbers)
print(result)        #>>> 720



#LOOPS
#with range() funcion:
output = []
for num in range(1,6):
    output.append(num)
    output.append(num + 0.5)

print(output[1:5])           # [1.5, 2, 2.5, 3, 3,5]


topping = input("enter a topping or write quit to stop:").lower
topping_list = []
price = 10

while True:
    topping = input("enter a topping or write quit to stop:").lower
    if topping == quit:
        print(f"Your toppings are: {','.join(topping_list)} and the price is {price}.")
        break
    else:
        print(f"You chose nothing to put on your pizza. The price is {price}")
        break 
else:
    topping_list.appe nd(topping)
    price += 2.50
    print(f"The {topping} is on your pizza now!")
    print(f"Your toppings are: {','.join(topping_list)} and the price is {price}.")