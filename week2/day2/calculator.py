# import modulesOperators

# def calculator():
#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))
#     op = input("Enter operation: ") 
#     if op == "+":
#         sum(num1,num2)
#     elif op == "*":
#         mult(num1,num2)
#     elif op == "-":
#         subt(num1,num2)
#     else: div(num1,num2)

# calculator()

from modulesOperators import sum, mult, subt, divis 

def calculator():
    num1 = int(input("Enter number: "))
    num2 = int(input("Enter second number: "))
    op = input("Enter operation: ")
    if op == "+":
        result = sum(num1,num2)
    elif op == "*":
        result = mult(num1,num2)
    elif op == "-":
        result = subt(num1,num2)
    elif op == "/":
        result = divis(num1,num2)    
    else:
        print("Invalid operator!")

    return result

print(calculator())