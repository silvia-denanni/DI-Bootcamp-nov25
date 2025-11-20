import string
import os 
import re

dir_path = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(dir_path, "Abracadabra.txt")

class Text:
    def __init__(self, input_text):
        self.text = input_text

    @classmethod
    def from_file(cls, file_path):              #cls refers to the class (Text), so you can create new instances inside this method
        with open(file_path, 'r') as file:
            content = file.read()               #reads ntire content of the file into the variable "content"
        return cls(content)                     #cls(content) which is the same as Text(content), creating a new Text object with the file content

# my_text = Text("Hello, world!")
# print(my_text.text)

    def word_frequency(self, word):
        words_list = self.text.split()          # splits the text into words (splitting on whitespace)
        count = words_list.count(word)          # counts how many times the given word appears (case-sensitive)                                       # returns count if found, else return a meaningful message
        if count > 0:                           # if the count is >0, it returns the number
            return count 
        else:
            return("None")

    def most_common_word(self):
        words_list = self.text.split()           # splits the text into words (splitting on whitespace) into a string
        word_frequency = {}                      # dictionary to store word frequencies, keys = words, values = counts
        for word in words_list:                  # finds the word with the highest frequency in word_list
            word_frequency[word] = word_frequency.get(word, 0) + 1   # if the word is not there yet = 0, then it becomes 1
        most_common_word = max(word_frequency, key = word_frequency.get)
        return most_common_word      #"key = word_frequency.get" compares words based on their values(key) in the dictionary
                                              
    def unique_words(self):
        words_list = self.text.split()
        unique = {}
        for word in words_list:
            unique[word] = unique.get(word, 0) + 1
        return list(unique.keys())            #returns all distinct words, not those that appear only once

text_instance = Text.from_file(file_path)
print(text_instance.text)
print(text_instance.unique_words())
print(text_instance.most_common_word())  
print(text_instance.word_frequency("tonight"))


class TextModification(Text):
    def __init__(self, input_text):
        super().__init__(input_text)
    
    def remove_punctuation(self):
        punctuation_characters = string.punctuation
        self.text = re.sub(r'[{}]'.format(re.escape(punctuation_characters)), '', self.text)
        return self.text
    
    

