picture = [[0,0,0,1,0,0,0],
           [0,0,1,1,1,0,0],
           [0,1,1,1,1,1,0],
           [0,0,1,1,1,0,0],
           [0,0,0,1,0,0,0],
           [0,0,0,0,0,0,0]
           ]
for row in picture:        #nested for loop
    for pixel in row: 
        if pixel == 1:
            print("*", end= " ")
        else:
            print(" ", end= " ")
    print('')


some_list = ["a", "b", "a", "c", "b"]

duplicates = []
for value in some_list:
    if some_list.count(value) > 1:   #nested conditionals
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)
        


