import os

class AnagramChecker:
    def __init__(self, word_list_file):
        self.words = set()         # Using a set for fast lookup and uniqueness

        fullpath = os.path.join(word_list_file,"wordList.txt")

        with open(fullpath, "r") as file_obj:             #w is "write", r is "read"
            for line in file_obj:
                word = line.strip().lower()       #removes any extra spaces or newline characters at the start or end + lowercase letters
                if word:                        # to skip blank lines
                    self.words.add(word)        #adds the cleaned lowercase word to the self.words set

    def is_valid_word(self, word): 
        if word.lower() in self.words:
            return True
        else:
            return False
    
    def is_anagram(self, word1, word2):
        w1 = word1.lower()                    # Normalize words to lowercase
        w2 = word2.lower()
        return sorted(w1) == sorted(w2) and w1 != w2   #returns the sorted words but in different letter order than before
    
    def get_anagrams(self, word):
        word = word.lower()     #lowercase letters ensure case insensitive comparison
        anagram_list = []
        for w in self.words:
            if self.is_anagram(word, w): #or each word w in the list, this line calls the is_anagram method to check if w is an anagram of the input word
                anagram_list.append(w)   #collects all matching anagrams in the anagram_list []
        return anagram_list              #if no anagrams are found, it returns an empty list.





       


    
        
