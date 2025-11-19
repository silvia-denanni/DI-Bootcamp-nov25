# What are built-in data structures? 
#1) lists
#2) tuples
#3) dictionaries
#4) sets

#1) LISTS
# list FUNCTIONS: append() AT THE END
#                 .insert() WHERE YOU WANT TO EXACTLY e.g. >>> l2.insert(1,6)
#                                                          >>> print(l2)
#                                                          >>> [2, 6, 3]
#                 count() counts the occurrences of a character/number
                  sorted() alphabetical order
                  sort() numerical order top to bottom
                  list slicing: technically not a built in function, works like one. e.g. lst = [1, 2, 3, 4, 5, 6, 7]
                                                                                          print(lst[::-1])
                                                                                          [7, 6, 5, 4, 3, 2, 1]
                  pop()        
                  remove()
                  clear()                                                                     

#2) TUPLES
# tuple functions: 
#--------------------------There is NO APPEND function in a tuple, but there is a workaround:
>>> t1 = (1, 2, 3, 4, 5)
>>> t2 = (6, 7, 8, 9)
>>> t3 = t1 + t2
>>> print(t3)
(1, 2, 3, 4, 5, 6, 7, 8, 9)

                 max(): prints a maximum value in the tuple
                 min(): prints a minimum value in the tuple
#3) DICTIONARIES
# dictionary functions: 
                       #pop() deletes certain key in the dictionary and returns it to you, e.g: 
                       cubes = {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}
                       print(cubes.pop(4))
                       print(cubes) #4
                                    # {1: 1, 2: 8, 3: 27, 5: 125}
                       #popitem() deletes the last element in the dictionary, e.g.
                       print(cubes.popitem())
                       print(cubes) #>>> (5, 125)
                                         #{1: 1, 2: 8, 3: 27}

                       #clear() erases all the key-value pairs in the dictionary, e.g.
                       cubes.clear()
                       print(cubes) #{}

                       #key() is used to access the key values in a dictionary, e.g.
                       dict = {1:'10', 2:'20', 3:'30', 4:'40', 5:'50'}
                       l1 =list(dict.keys())
                       print("the key values are:")
                       print(l1)    # the key values are: [1, 2, 3, 4, 5]
                       
                       #values() is used to access the values of dictionary
                       #items() is used to access the key-value pair

# 4) SETS are a collection that is UNORDERED and UNINDEXED
# set functions:        remove() function removes certain elements in the set, e.g.
                        set1 = {1, 2, 3, 4, "hi", "world", "python"}
                        set1.remove(4)
                        print(set1) #>>> {1, 2, 3, 'world', 'python', 'hi'}