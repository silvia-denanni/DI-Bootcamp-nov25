#LOOPS AND DICTIONARIES
my_books = {
  "title": "The Hunger Games",
  "author": "Susan Collins",
}

for x, y in my_books.items():
    print("The " + x + " is " + y + ".")  #-->  >>>The title is The Hunger Games.
                                          #    >>> The author is Susan Collins.

#LOOPS OPERATORS

 #1)RANGES: range() they make us create a sequence of numbers

  # STRUCTURE: for num in range(1,11,2) ---------> the numbers mean: (1 START, 2 STOP, 3 STEP)

for num in range(1,11):
    print(num)       # it prints from 1 to 10 INCLUDING LAST NUMBER (that is why you need "11")

for num in range(1,11,2):
    print(num)      # it prints from 1 to 10, only the ODD 
#-------------------------if you want to use STEP, you need to put ALL OF THE NUMBER REFERENCES

 #2)ENUMERATING: enumerate() returns a tuple with index and item

# hogwarts_students = ["Harry", "Potter", 15, "Privet Drive", "Hedwig", "Buckbeak"]

#-----------------------------------------------hogwarts_students[0] = hogwarts_students[0].lower() ---> changing with no
#                                               for loop

#Simple Example
for element in enumerate('abcd'):
    print(element)            #>>>(0, 'a') -----> 0 = index; a = item
                              # (1, 'b')
                              # (2, 'c')
                              # (3, 'd')

#Complex Example 
hogwarts_students = ["Harry", "Potter", 15, "Privet Drive", "Hedwig", "Buckbeak"]
for i, item in enumerate(hogwarts_students):  #access to both index and item
    if type(item) == str:     #we check if the item is a string -- type() FUNCTION
        hogwarts_students(i) = item.lower()   #we change the item in the dictionary to lowercase

print(hogwarts_students)  

 #3)ZIP: CONCATENATES iterables in a TUPLE -->zip()

list1 = [1,2,3]
list2 = ['a','b','c']
list3 = [1.1, 2.2, 3.3, 4.4, 5.5]

for item in zip(list1, list2, list3):
    print(item)      # >>> (1, 'a', 1.1)
                     # (2, 'b', 2.2)
                     # (3, 'c', 3.3)


