#DICTIONARIES ARE MORE COMPLEX SEQUENCES, with KEY/VALUE PAIRS
student_info = ["Harry", "Potter", 15, "Privet Drive", "Hedwig", "Buckbeak"]
#THIS IS A LIST, NOT REALLY THE BEST FORMAT FOR WHAT WE ARE TRYING TO DO ABOVE
student_info_dic = {"first name":"Harry",
                    "surname":"Potter",
                    "age":15,
                    "address":"Privet Drive",
                    "pets":["Hedwig","Buckbeak"],   #list
                    "best_friends":("Ron Weasley", "Hermione Granger"),  #tuple
                    "is parselmouth":True,
                    "house":{"main": "Gryffyndor","secondary":"Slytherin"}}  #dictionary
#You can put inside lists, tuples, booleans, dictionaries....
# A KEY HAS TO BE UNIQUE! 
                                            #How to access data in a dictionary?
student_info_dic = {"first name":"Harry",
                    "surname":"Potter",
                    "age":15,
                    "address":"Privet Drive",
                    "pets":["Hedwig","Buckbeak"],   #list
                    "best_friends":("Ron Weasley", "Hermione Granger"),  #tuple
                    "is parselmouth":True,
                    "house":{"main": "Gryffyndor","secondary":"Slytherin"}} 

print(student_info_dic["first name"])
print(student_info_dic["pets"[1]])        #by inputting in [] the index number

#TO AVOID ERRORS, IF A KEY WE ARE LOOKING FOR IS NOT FEATURED IN THE DICTIONARY, WE USE:
#---------------------------------------.get() FUNCTION ------------------------>
user_dictionary = {"name": "Spike", "age": 118,}
print(user_dictionary.get("hair color"))  #>>>None INSTEAD OOF !Error

                                           # HOW TO ADD DATA IN A DICTIONARY?
student_info_dic["pets"].append("Toby")
print(student_info_dic)

                                                  #HOW DO YOU MODIFY VALUES?

student_info_dic["house"].upper("main")
print(student_info_dic)


                                                  #HOW DO YOU REPLACE VALUES?
student_info_dic["first name"] = "Thiago"
print(student_info_dic)

                                                       #EXERCISE IN CLASS
# print Harry's age
# add 10 years to it, print it again
# change the address to "Bezalel, 8"
# add a new pet to the pets list
# change the boolean to false

student_info = {"first_name":"Harry",
               "surname":"Potter",
               "age":15,
               "address":"Privet Drive",
               "pets":["Hedwig","Buckbeak"],  
               "best_friends":("Ron Weasley", "Hermione Granger"), 
               "is parselmouth":True,
               "house":{"main": "Gryffyndor","secondary":"Slytherin"}}  

print(student_info["first_name"])
student_info["age"] += 10
print(student_info)
student_info["pets"].append("Tuli")
print(student_info)
student_info["address"] = "Bezalel, 8"
print(student_info)
student_info["is parselmouth"] = "False"
print(student_info)

                                           #ADDING A NEW KEY VALUE PAIR IN A DICTIONARY 2 WAYS
#WAY 1
student_info = {"first_name":"Harry",
               "surname":"Potter",
               "age":15,
               "address":"Privet Drive",
               "pets":["Hedwig","Buckbeak"],  
               "best_friends":("Ron Weasley", "Hermione Granger"), 
               "is parselmouth":True,
               "house":{"main": "Gryffyndor","secondary":"Slytherin"}}  

student_info["teachers"] = "Snape"
print(student_info)                   #>>> {{'first_name': .........'principal': 'Dumbledore'}

#WAY 2                             
                                   
student_info = {"first_name":"Harry",
               "surname":"Potter",
               "age":15,
               "address":"Privet Drive",
               "pets":["Hedwig","Buckbeak"],  
               "best_friends":("Ron Weasley", "Hermione Granger"), 
               "is parselmouth":True,
               "house":{"main": "Gryffyndor","secondary":"Slytherin"}} 

student_info.update({"principal":"Dumbledore"})
print(student_info)      #>>> {{'first_name': .........'principal': 'Dumbledore'}


# --------------------------------------.get ONLY lets us ASSIGN A NEW KEY, BY PROVIDING IT with a value:
user_dictionary = {"name": "Spike", "age": 118,}
print(user_dictionary.get("hair color", "platinum blonde")) #>>> platinum blonde


                                  #DELETING A KEY VALUE PAIR IN A DICTIONARY

del student_info["address"]
print(student_info)


                                                #EXERCISE IN CLASS: Retrieve the history mark ONLY:

sample_dict = { 
   "class":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics":70,
            "history":80
         }
      }
   }
}

history_mark = sample_dict["class"]["student"]["marks"]["history"]  #THIS METHOD ONLY WORKS IN A NESTED DICT!!!!!!!!!!!
print(history_mark)           #>>>80



#zip() FUNCTION can be used with any type of sequence, TO CONCATENATE 

name_list = ("silvia", "elettra", "michela", "daniela") #tuple
city_list = ["zeitan", "ittiri", "fara gera dadda", "san giuliano milanese"] #dictionary

name_cities = dict(zip(name_list,city_list))   #dict() "dictionarizes" zip() lists
print(name_cities)


#DICTIONARY LOOPS

                                                #STRUCTURE GENERIC
                                      #for item in dictionary:
                                      #    print(item)

#to ACCESS KEYS ONLY through a LOOP --> DICTIONARYNAME.keys() FUNCTION:
student_info = {"first_name":"Harry",
               "surname":"Potter",
               "age":15,
               "address":"Privet Drive",
               "pets":["Hedwig","Buckbeak"],  
               "best_friends":("Ron Weasley", "Hermione Granger"), 
               "is parselmouth":True,
               "house":{"main": "Gryffyndor","secondary":"Slytherin"}} 

for key in student_info.keys():        # .keys() FUNCTION:
    print(key)              #first_name
                            #surname
                            #...

#access only VALUES through a loop --> DICTIONARYNAME.values()

for value in student_info.values():
    print(value)            #Harry
                            #Potter
                            #...

#access BOTH KEYS & VALUES through a loop --> DICTIONARYNAME.items()
for key, value in student_info.items():
    print(key,value)       #first_name Harry
                           #surname Potter

#EXERCISE: change all the string values to uppercase

student_info = {"first_name":"Harry",
               "surname":"Potter",
               "age":15,
               "address":"Privet Drive",
               "pets":["Hedwig","Buckbeak"],  
               "best_friends":("Ron Weasley", "Hermione Granger"), 
               "is parselmouth":True,
               "house":{"main": "Gryffyndor","secondary":"Slytherin"}} 

for key, value in student_info.items():
    if type(value) == str:
        student_info[key] = value.upper()
        print(student_info)      #{'first_name': 'HARRY', 'surname': 'POTTER', 'age': 15, 
                                 #    'address': 'PRIVET DRIVE', 'pets': ['Hedwig', 'Buckbeak'],
                                 # 'best_friends': ('Ron Weasley', 'Hermione Granger'), 'is parselmouth': True, 
                                 #   'house': {'main': 'Gryffyndor', 'secondary': 'Slytherin'}}


