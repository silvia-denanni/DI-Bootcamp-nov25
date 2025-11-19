#WHAT IS A SCOPE? 

fav_movie = "American Beauty"    #global scope --> IT IS VALID FOR ALL OF THE SHEET

#WHEN WE CREATE A FUNCTION def function_name():, we CREATE A LOCAL SCOPE: IT CANNOT BE ACCESSED OUTSIDE OT IT
def movie_recommend(fav_movie):
    recommendation = "American Hustle" #LOCAL SCOPE
    return recommendation #the info IS UNACCESSIBLE GLOBALLY
print(movie_recommend(fav_movie))  #>>> ERROR name 'recommendation' is not defined --> this variable is local, 
                                       #cannot be accessed!
print(fav_movie)


savings = 500                   # GLOBAL scope variable
def buy_stuff(amount):
    if amount < savings:        #CAN BE CALLED LOCALLY
        return True
    else:
        return False    
print(buy_stuff(600))            #>>> False

               # JOLLY: global KEYWORD
savings = 500
def buy_stuff(amount):
    global savings    #global KW MAKES LOCAL VARIABLES GLOBAL, USE WITH CAUTION!
                      #global VARIABLES CAN BE CONSULTED FOR LOCAL SCOPE, BUT NOT CHANGED
    savings -= 100    #this way the amount can be subtracted, because before it wasn't accessible
    print(savings)
    if amount < savings:
        return True
    else:
        return False    
print(buy_stuff(600))              

#USING GLOBAL OR NOT?

total = 0

def count():
    global total
    total += 1
    return total

count()
count()
print(count())      #>>>3

#                         ---------------IT IS BETTER TO DO THIS INSTEAD: 

total = 0

def count(total):                #DEPENDENCY INJECTION
    total += 1
    return total

print(3)  #>>>3            it is like saying --> print(count(count(count(total))))