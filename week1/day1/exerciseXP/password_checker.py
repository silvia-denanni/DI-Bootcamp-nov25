username = input("What is your username? ")
password = input("What is your password? ")
# if username == "shirubia" and password == "m4d4u":
#     print(f"{username}, your password {password} is {len(password)} letters long.")
password_lenght = len(password)
hidden_password = "*" * password_lenght
#print("*" * 5)
print(f"{username}, your password {password} is {len(password)} letters long.")