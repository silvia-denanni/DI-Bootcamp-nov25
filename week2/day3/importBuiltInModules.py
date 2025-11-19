#IMPORTING BUILTIN PYtHON MODULES: sYNTAX

# import moduleName                   call a module
# moduleName.function()               use module function

import math
print("The value of cosine is", math.cos(3))   #>>> The value of cosine is -0.9899924966004454
print("The value of sine is", math.sin(3))     #>>> The value of sine is 0.1411200080598672
print("The value of tangent is", math.tan(3))  #>>> The value of tangent is -0.1425465430742778
print("The value of pi is", math.pi)           #>>> The value of pi is 3.141592653589793



# COLLECTIONS 
# Collections are DATA STRUCTURES (like lists, tuples, dictionaries, sets) and python has many BUILT-IN ones -->

# 6 COLLECTIONS MODULES
#           ------->    from collections import "CollectionName"  <-------- HOW TO ACCESS

# 1. Defaultdict
# 2. Counter
# 3. Deque
# 4. Namedtuple()
# 5. ChainMap
# 6. OrderedDict

#1 DEFAULTDICT
# is exactly like a dictionary in python BUT it does NOT give an EXCEPTION/ERROR when you try to access the
# non-existent key.

from collections import defaultdict  
nums = defaultdict(int)  
nums['one'] = 1  
nums['two'] = 2
nums['three'] = 3 
print(nums['four'])   #>>> 0 (INSTEAD OF Error)

#2 COUNTER
# built-in data structure which is used to count the occurrence of each value present in an array or list
from collections import Counter  
list = [1,2,3,4,1,2,6,7,3,8,1,2,2]  
answer=Counter()
answer = Counter(list)  
print(answer[2])  # 4 ---> 2 is in the list 4 TIMES


#3 DEQUE
#  It can add/remove items from either start or the end of the list.

from collections import deque  
#initialization
list = ["a","b","c"]  
deq = deque(list)  
print(deq)      #>>> deque(['a', 'b', 'c'])

#insertion
deq.append("z")   #ADD TO THE END
deq.appendleft("g")    #ADD TO THE BEGINNING (left of the lsit)
print(deq)      #>>> deque(['g', 'a', 'b', 'c', 'z'])

#removal
deq.pop()  
deq.popleft()  
print(deq)    #>>> deque(['a', 'b', 'c'])   ---> REMOVED all of the ADDITIONS BEFORE

# 4 NAMEDTUPLE
# Usual tuples need to remember the INDEX of each FIELD of a TUPLE OBJECT ---> 
# namedtuple() solves this by simply returning with names for each position in the tuple

from collections import namedtuple
Student = namedtuple('Student', 'name, surname, age')  
student1 = Student('Peter', 'James', '13')  
print(student1.name)    #>>> Peter


#INSTEAD OF REGULAR TUPLE ACCESSING through INDEX:

student1 = ('Peter', 'James', '13')
print(student1[0])  #>>> 'Peter'

#-------------------->  student1.name == student1[0] to access the first element "first name"<--------------------- 


# 5 CHAINMAPS
# COMBINES MANY DICTIONARIES TOGETHER and returns a list of dictionaries with NO RESTRICTION on their number

import collections

dictionary1 = { 'a' : 1, 'b' : 2 }  
dictionary2 = { 'c' : 3, 'b' : 4 }  
chain_Map = collections.ChainMap(dictionary1, dictionary2)  
print(chain_Map.maps)   #>>> [{'a': 1, 'b': 2}, {'c': 3, 'b': 4}]

# 6 ORDEREDDICT
# is a dictionary that ensures its ORDER is MANTAINED: if the keys are inserted in a specific order,
# then the order is MANTAINED, EVEN IF YOU CHANGE the value of the key later

from collections import OrderedDict  
orderd = OrderedDict()  
orderd['a'] = 1  
orderd['b'] = 2  
orderd['c'] = 3  
print(orderd) #>>> OrderedDict({'a': 1, 'b': 2, 'c': 3})

#unordered dictionary
unordered=dict()
unordered['a'] = 1  
unordered['b'] = 2  
unordered['c'] = 3 
print("Default dictionary", unordered)  #>>> Default dictionary {'a': 1, 'b': 2, 'c': 3}


#PYTHON ITERTOOLS FUNCTION MODULE
#needs to be IMPORTED* and is used to ITERATE over data structures/ITERABLES that can be stepped over with a for-loop

#the IterTools module has many different FUNCTIONS, categorizable in 2 types:
# 1 - INFINITE ITERATORS : count ---- cycle ---- repeat
# 2 - FINITE ITERATORS : chain ---- compress ---- dropwhile

#*import itertools

# INFINITE ITERATORS : 1) COUNT 

import itertools

result = itertools.count(start = 0, step = 2)  
for number in result:
# termination condition
    if number < 8:              #print the first four even numbers --> BREAK
        print (number)
    else:
        break            #>>> 0
                            # 2
                            # 4
                            # 6


# INFINITE ITERATORS : 2) CICLE --> takes in an iterable and goes over it INDEFINITELY

import itertools

result = itertools.cycle('12345')
counter = 0

for number in result:
# termination condition
    if counter < 10 :
        print (number)
        counter = counter + 1        # print 2 times three
    else:
        break                         #>>> 1
                                        #  2
                                        #  3
                                        #  4
                                        #  5
                                        #  1
                                        #  2
                                        #  3
                                        #  4 
                                        #  5
        
# INFINITE ITERATORS : 3) REPEAT - 
# This function takes an iterable and iterates over it indefinitely but != CICLE because:
# ------> Takes an optional "TIMES" parameter that can be used as a termination condition
import itertools

result = itertools.repeat('hello', times = 2)   #print hello two times

for word in result:
    print (word)                #>>> hello
                                    #hello


# FINITE ITERATORS : 1) CHAIN 
# accepts a variable number of iterables and loops through all of them, one by one

import itertools

list_one = ['a', 'b', 'c']
list_two =['d', 'e', 'f']
list_three = ['1', '2', '3']

result = itertools.chain(list_one, list_two, list_three)     # iterate over three lists

for element in result:
  print (element)          #>>> a b c d e f 1 2 3 (but vertically)                       

# FINITE ITERATORS : 2) COMPRESS
#  takes in an iterable and a selector, and RETURNS an iterable with ONLY
#  those items for which the corresponding SELECTOR value is TRUE

import itertools

names = ['Alice', 'James', 'Matt']
have_flu = [True, True, False]

result = itertools.compress(names, have_flu)   #ITERABLE: names of people SELECTOR: who have the flu ONLY

for element in result:
  print (element)     #>>> Alice
                        #  James

 
# FINITE ITERATORS : 3) DROPWHILE
# an ITERABLE and a FUNCTION (predefined or LAMDA) is passed to it
# keeps on dropping values from the iterable until it encounters the FIRST ELEMENT that evaluates to FALSE

import itertools

my_list = [0, 0, 1, 2, 0]

result = itertools.dropwhile(lambda x: x == 0, my_list)

for elements in result:
  print (elements)   #>>> 1
                     #    2
                     #    0



