# Exercise 1: Random Sentence Generator
import os 
import random

dir_path = os.path.dirname(os.path.realpath(__file__))

def get_words_from_file(file_path):

    full_path = os.path.join(dir_path, file_path)   # Use os.path.join to build the full path correctly on any OS
    with open(full_path, "r") as file:
        content = file.read()        #new temp variable that holds the entire text as one big string
    words = content.split()          #new temp variable that splits the big string content into a list of words
    return words
#print(get_words_from_file(dir_path))       #it prints all of the word list      

def get_random_sentence(sentence_length, file_path):
    words = get_words_from_file(file_path)   # calls the first function 
    chosen_words = [random.choice(words) for _ in range(sentence_length)] #selects a random word from the list "sentence length" times, "_" is just a placeholder since we don’t need the loop variable
    sentence = " ".join(chosen_words).lower   #Create a sentence with the selected words in lowercase 
    return sentence

def main():
    print("This program will build a random sentence from words chosen from a list of equally random words.")
    sentence_input = (input("Please choose your sentence lenght: enter a number between 2 and 20: "))
  
    if not sentence_input.isdigit: 
        print("Invalid non integer input...reinitializing")
        return
    
    sentence_length = int(sentence_input)
    
    if sentence_length < 2 or sentence_length > 20:
        print("Invalid input: number not in range 2 to 20. Exiting.")
        return
    
    print("Input accepted!")
    random_sentence = get_random_sentence(sentence_length,"wordList.txt")

    print("Generated sentence: ")
    print(random_sentence())
    
if __name__ == "__main__":
    main()                         #guard to allow importing without running main()


#Exercise 2: Working with JSON

import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

# json_file = "my_XPfile.json"
# with open(json_file, 'w') as file_obj:
#     json.dump(sampleJson, file_obj)     --->this is passing a string (sampleJson) to json.dump(), not a Python dictionary

data = json.loads(sampleJson)

'''Access the nested “salary” key.'''

salary = data["company"]["employee"]["payable"]["salary"]
print(salary)   #7000

'''# Add a new key “birth_date” to the “employee” dictionary'''

data["company"]["employee"]["bith_date"] = "1990-01-01"
print(json.dumps(data, indent=4))             #------------------------------->
 
'''{
    "company": {
        "employee": {
            "name": "emma",
            "payable": {
                "salary": 7000,
                "bonus": 800
            },
            "bith_date": "1990-01-01"
        }
    }
}'''

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(dir_path + '\my_XPfile.json', 'r') as f:
    my_XPfile = json.load(f)                 # .load to convert a JSON file into a dict in python
    print(my_XPfile)             #>>> {'company': {'employee': {'name': 'emma', 'payable': {'salary': 7000, 'bonus': 800}, 'bith_date': '1990-01-01'}}}
    print(type(my_XPfile))       #>>> <class 'dict'>

json_file = "my_XPfile.json"
with open(json_file, 'w') as file_obj:
    json.dump(data, file_obj, indent=4)  # indent=4 for pretty-printed
