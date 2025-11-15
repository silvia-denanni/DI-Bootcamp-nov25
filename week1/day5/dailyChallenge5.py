#Challenge 1: Sorting

# Write a Python program that takes a single string of words as input, where the words are separated by commas 
# (e.g., ‘apple,banana,cherry’). The program should output these words sorted in alphabetical order, with the sorted 
#  words also separated by commas.

user_string = input("Input words separated by commas - e.g. apple,banana,cherry, etc. ")   #single string of words as input

string_array = user_string.split(",") 
string_array.sort()

sorted_string = ",".join(string_array)
print(sorted_string)

#Challenge 2: Longest Word
# Write a function that takes a sentence as input and returns the longest word in the sentence.
# If there are multiple longest words, return the first one encountered. 
# Characters like apostrophes, commas, and periods should be considered part of the word.

#Define a function that takes a string (the sentence) as a parameter.

def user_sentence():
    user_input = input("Write a sentence and I will give you back the longest word in it: ")
    return user_input  # Return the input string so other parts of the program can use it

def find_longest_word(sentence):                    # the input of this new function is a string of words (sentence)
    split_user_sentence = sentence.split((" "))     # the split sentence is saved in variable "split_user_sentence"
    longest_word = ""                               #  This will hold the longest word we find.
    max_lenght = 0                             # This will keep track of the length of the longest word found so far          
    for word in split_user_sentence:
        if len(word) > max_lenght:
            longest_word = word
            max_lenght = len(word)
    return longest_word  # Return the longest word found

sentence = user_sentence()   #We call the user_sentence() function to get the sentence from the user and save it in the variable sentence
longest = find_longest_word(sentence) #We call the user_sentence() function to get the sentence from the user and save it in the variable sentence
print("The longest word is:", longest)
