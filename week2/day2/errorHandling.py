# while True:
#     try:
#         age = int(input("Enter your age: "))
#         10/age
#     except ValueError:                                  #it renders error catching more descriptive
#         print("Please enter a number: ")
#     except ZeroDivisionError:
#         print ("Please enter a number bigger than zero.")
#     else:
#         print("Thank you!")
#         break 

def sum(a,b):
    try:
        return a+b
    except TypeError as e:
        print("Please enter a number {e}")     #IT GIVES ME BACK THE ERROR DESCRIPTION IN CASE OF TYPING ERROR (error types are built-in in python)

print(sum("3",4))                 #Please enter a number
    

