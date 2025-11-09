for item in (1,2,3,4,5):
 for x in ["a", "b", "c", "d", "e"]:
  print(item, x)

i = 0
while i < 50:
 print(i)
 i = i + 1 #or i += 1, it is the same (augmented assigned operator way)

i = 0
while i < 50:
 print(i)
 i = i + 1
 break
else: 
 print("done")
 #"break" and right after "else" can happen one after the other in a while loop only when we want that the else group executes when there isn't a "break" statement (very rare occurrence)

 for i in range(2):
  print (list(range(10))) #RIVEDERE

 #UNPACKING TUPLES:

#Traditionally, to SWAPvalues of two variables, you would use a TEMPORARY VARIABLE like this (in this case TMP):
x = 10
y = 20

print(f'x={x}, y={y}')

tmp = x
x = y
y = tmp

print(f'x={x}, y={y}') #Output:
# x=10, y=20
# x=20, y=10  

#In Python, you can use the unpacking tuple syntax to achieve the same result:
x = 10
y = 20

print(f'x={x}, y={y}')

x, y = y, x

print(f'x={x}, y={y}') #OUTPUT x=10, y=20
# x=20, y=10 --> Python uses the commas (,) to define a tuple, not parentheses.

# DICTIONARIES: USING TUPLE UNPACKING TO ITERATE THROUGH THE VALUES by using the .ITEMS()METHOD -->

a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}

print(a_dict.items())

#FOR LOOP within dictionary (same as in the 2 lines right above here):
for key, value in a_dict.items():
    print(key, '->', value)

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
# print(sample_dict["marks"]) ---> MISTAKE cause it is not the first element in the dict. CORRECT -->

print(sample_dict["class"]["student"]["marks"]["history"])
 
#  sample_dict["class"]accesses the dictionary under the key "class".
# ["student"] accesses the dictionary under "student" inside "class".
# ["marks"] accesses the "marks" dictionary inside "student".
#["history" accesses the history mark only.

# sample_dict = { 
#    "class":{ 
#       "student":{ 
#          "name":"Mike",
#          "marks":{ 
#             "physics":70,
#             "history":80
#          }
#       }
#    }
# }
# sample_dict["class"] = "year"

sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"

}
sample_dict.pop("name")
print(sample_dict)