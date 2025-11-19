#1
# Ask the user for two inputs:
# A number (integer).
# A length (integer).
# 2. Create a program that generates a list of multiples of the given number.
# 3. The list should stop when it reaches the length specified by the user.
number = int(input("Enter an integer number: "))
length = int(input("Enter the length of the multiples list: "))
multiples = [number * i for i in range(1, length + 1)] #LIST COMPREHENSION 
print(f"The first {length} multiples of {number} are: {multiples}")

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