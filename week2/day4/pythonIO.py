import os 

#python I/O --> Input/Output

#OLD SCHOOL WAY: OPENING FILES ----> CLOSING THEM WAS PROBLEMATIC

# f = open('secrets.txt')
# secret_data = f.read()
# # secret_data is a string
# f.close()           #  NOT THE SAFEST WAY TO CLOSE  -->


# try:
#    f = open("secrets.txt",encoding = 'utf-8')
#    # perform file operations
# finally:
#    f.close()                    # SAFER WAY TO CLOSE


#NEW SCHOOL WAY: WITH STATEMENT

#-----------------------import os---------SOLUTION to actually FIND THE FILE------------------------------------------

# with open("secrets.txt", "r") as file_obj:             #w is "write", r is "read"
#    print(file_obj.read())                              #>>>Error file not found

dir_path = os.path.dirname(os.path.realpath(__file__))  #FONDAMENTALEEEEEEEEEEEEEEEEEEEEEEEEE it gives us THE FULL PATH

with open(dir_path + "\starwars.txt", "r") as file_obj:             #w is "write", r is "read"
   content = file_obj.read() 
   print(content)  


txt_list =  #CAZZZOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO

for line in txt_list:
   print(line)
print("End of doc.")

print(txt_list[4])

print(txt_list[:5])

#EXERCISE Read all the file and return it as a list of strings. Then split each word into letters

temp_list = []
for name in txt_list:
   temp_list.append(list(name))

print(temp_list)

# Find out how many occurences of the names "Darth", "Luke" and "Lea" are in the file

counts ={"Darth": 0, "Luke": 0, "Lea":0}
for name in txt_list:
    if name == "Darth":
      counts["Darth"] += 1
    elif name == "Luke":
      counts["Luke"] += 1
    elif name == "Lea":
      counts["Lea"] += 1
print(counts)

#OR BETTER: .COUNT

full_txt_str = "".join(text_list)

counts ={"Darth": full_txt_str.count("Darth"),
         "Luke": full_txt_str.count("Luke"),
         "Lea": full_txt_str.count("Lea")}

print(counts)

#Append your first name at the end of the file

with open(dir_path + "\starwars.txt", "a+") as f:             #w is "write", r is "read"
    f.seek(0,os.SEEK_END)
    f.write("\nSilvia")
    print("Successfully added!")

#Append "SkyWalker" next to each first name "Luke"

with open(dir_path + "\starwars.txt", "r+") as f:
    txt_list = f.readlines()
    modified_content = []

    for name in txt_list:
        if name == "Luke\n":
           modified_content.append("Luke Skywalker\n")
        else:
            modified_content.append(name)
                                   
with open(dir_path + "\starwars.txt", "w", encoding="utf-8") as f:
     f.seek(0)
     f.writelines(modified_content)                          
     print("Skywalker was added")




