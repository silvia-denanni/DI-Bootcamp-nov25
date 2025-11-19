#1
# Ask the user for two inputs:
# A number (integer).
# A length (integer).
# 2. Create a program that generates a list of multiples of the given number.
# 3. The list should stop when it reaches the length specified by the user.
number = int(input("Enter an integer number: "))
length = int(input("Enter the length of the multiples list: "))
multiples = [number * i for i in range(1, length + 1)] #LIST COMPREHENSIO*N
print(f"The first {length} multiples of {number} are: {multiples}")

#]*LIST COMPREHENSION
# multiples = [number * i for i in range(1, length + 1)]

# BROKEN INTO PIECES

# for i in range(1, length + 1) -> Loop that goes from 1 to the lenght of the inputted number, including 
#                                  lenght (+1)
#number * i  -> For each value of i, this expression calculates the product of number and i
#[ ... ] -> The square brackets mean "create a list" from all the results of number * i as i goes 
            #goes trough the range.

# IN A NUTSHELL
# The list comprehension runs the loop internally.
# For each i, it calculates number * i.
# It collects all these results into a new list.
# This new list is assigned to the variable multiples.


#2
# 1. Ask the user for a string.
# 2. Write a program that processes the string to remove consecutive duplicate letters.
# The new string should only contain unique consecutive letters.
# For example, “ppoeemm” should become “poem” (removes consecutive duplicates like ‘pp’, ‘ee’, and ‘mm’).
# 3. The program should print the modified string.
# Example
# Input:
# user’s word: "ppoeemm"
# Output:
# "poem"

user_input = input("Enter a string: ")
result = ""
for char in user_input:
    if len(result) == 0 or char != result[-1]:
        result += char
print(result)

# BROKEN INTO PIECES

# len(result) == 0 -> is necessary to handle the very first character being added to the result string
#                      when the program starts, it results in an empty string ("")
# char != result[-1] -> it is a condition that compares the current character "char" with the latest entered

# -------- if result is empty, trying to access "result[-1]"
#  would cause an error because there is no last character to compare to ---------

# -> if result is empty (len(result) == 0), the program adds the first character without comparison
# -> now result is no longer empty, so the program can safely compare the current character with the last 
#    character in result to decide whether to add it or skip it

# IN A NUTSHELL

# LENGHT CHECK is a safe way to avoid errors and ensure THE FIRST CHARACTER IS ALWAYS ADDED
# to the result BEFORE starting comparisons