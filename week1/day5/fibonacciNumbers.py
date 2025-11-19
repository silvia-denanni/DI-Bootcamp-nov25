def fibonacci(number):
    a = 0
    b = 1
    for x in range(number):
        yield a     # function that asks for the next item until the generator is done
        temp = a
        a = b
        b = temp + b

for number in fibonacci(11):
    print(number)

#DOING THE SAME BUT IN A LIST

def fibonacci2(number):
    a = 0
    b = 1
    result = []

    for n in range(number):
        result.append(a)
        temp = a
        a = b
        b = temp + b
    return result

print(fibonacci2(16))