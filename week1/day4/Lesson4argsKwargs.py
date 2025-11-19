* (unpacking operator) ARGS
** (unpacking operator) KWARGS

# *ARGS: arguments --> you don't know how many REGULAR ARGUMENTS we need to pass in a function
# **KWARGS: keyword arguments -->  we don’t know in advance how KW ARGUMENTS we need to pass in a function
                                  # very specific and difficult to "recycle" later in the program

friends = ["Ross", "Rachel", "Monica", "Joey", "Phoebe", "Chandler"]

# def how_you_doing(*args):   #* from 0 to millions, needs to be specified
#     if args:                #* IF --> SPECIFIES 
#         for name in args:
#             return(f"{name}, how you doing?")        #return is also a break, you cannot use it inside a loop
# print(how_you_doing("Ross", "Rachel", "Monica", "Joey", "Phoebe", "Chandler")) # --> ERROR



friends = ["Ross", "Rachel", "Monica", "Joey", "Phoebe", "Chandler"] # global 

def how_you_doing(*args):   #* from 0 to millions, needs to be specified, so 
    if args:                #* IF --> SPECIFIES 
        for name in args:
            return(f"{name}, how you doing?")
        else:
            print("Please enter names!")

print(how_you_doing("Ross", "Rachel", "Monica", "Joey", "Phoebe", "Chandler"))
                                        #OR
print(how_you_doing()) # because I have the global value "friends" ON TOP


#KWARGS CALLING FUNCTION

def user_info(**kwargs):
    print(kwargs)
for value in kwargs.values():
    print(value)

user_info(name = "Ross", last_name = "Geller", #etc.)
          