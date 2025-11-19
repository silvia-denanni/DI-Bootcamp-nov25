import os
dir_path = os.path.dirname(os.path.realpath(__file__))

# --------------Only STRINGS,NUMBERS, BOOLEANS, DICTIONARIES, LISTS, TUPLES or NONE can be converted to JSON-------------------

#CONVERTING A PYTHON DICTIONARY INTO A JSON FILE
import json                #FUNDAMENTAL TO WORK WITH JSON

my_family = {
    "parents":['Beth', 'Jerry'],
    "children":['Summer', 'Morty']
}
            # json.dump() transforms my_family to a JSON string which will be saved in the my_file.json file:

'''!!!!!!ATTENTION!!!!!!'''
'''The destination file should be a FILE OBJECT and not a filename --->
                                To get a file object, use the OPEN function.'''


with open(dir_path + '\my_family.json', 'w') as f:              #f is file object
    json.dump(my_family, f)                                  #creating a JSON file "my_family" with .DUMP
    print("file was created")         #>>>file was created           ---->"my_family"

#convert a python dict in a JSON string (short data)

my_family_json = json.dumps(my_family)              #dumps --> the s is for string
print(my_family_json)             #>>> {"parents": ["Beth", "Jerry"], "children": ["Summer", "Morty"]}

'''FROM python dict to JSON but make it PRETTY'''

import json

my_family = {
    "parents" :['Beth', 'Jerry'],
    "children" :['Summer', 'Morty']
}
json_file = "index.json"
with open(json_file, 'w') as file_obj:
    json.dump(my_family, file_obj, indent = 2, sort_keys=True)

'''{
  "children": [
    "Summer",
    "Morty"
  ],
  "parents": [
    "Beth",
    "Jerry"
  ]
}'''

#a JSON file to convert into a dict in python
with open(dir_path + '\my_family.json', 'r') as f:
    my_family2 = json.load(f)                 # .load to convert a JSON file into a dict in python
    print(my_family2)            #>>> {"parents": ["Beth", "Jerry"], "children": ["Summer", "Morty"]} 
    print(type(my_family2))                              #>>> <class 'dict'>


#JSON string to convert into a dict in python

my_family3 = json.loads(my_family_json)
#print(type(my_family3))                                  #>>> <class 'dict'>
print(my_family3)                 #>>> {'parents': ['Beth', 'Jerry'], 'children': ['Summer', 'Morty']}




