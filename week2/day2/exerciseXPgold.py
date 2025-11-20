# class BankAccount():
#     def __init__(self, balance, username, password, authenticated = False):
#         self.balance = balance
    
#     def authenticate(self, username, password, authenticated):
#         username_string = username
#         password_string = password
#         if username_string and password_string == username and password:
#             authenticated = True
#         else:
#             authenticated = False
#         return authenticated

#     def deposit(self, user_input, authenticated):
#         while authenticated == True:
#             try:
#                 user_input = int(input("Please enter a number: ")) 
#                 balance += user_input
#                 return balance
#             except:
#                 print(input("You entered either an incorrect username or password. Please try again: "))
#                 break
            
#     def withdraw(self, user_deduction):
#         self.user_deduction = input("Please enter a number: ")
#         balance -= user_deduction
#         if user_deduction is not int:
#             try:
#                 print("Please enter a number that is bigger than 0!")
#             except:
#                 return balance

            
# class MinimumBalanceAccount(BankAccount):
#     def __init__(self, balance, minimum_balance = 0):
#         self.balance = balance
#         self.minimum_balance = minimum_balance
    
#     def override_withdrawal(balance, minimum_balance):
#         while minimum_balance < balance:
            

class BankAccount():
    def __init__(self, balance, username, password):
        self.balance = balance
        self.username = username
        self.password = password
        self.authenticated = False
    
    def authenticate(self, username, password):
        if username == self.username and password == self.password:
            self.authenticated = True
        else:
            self.authenticated = False
        return self.authenticated

    def deposit(self, amount):
        if not self.authenticated:
            raise Exception("User not authenticated. Please login first.")
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        return self.balance
            
    def withdraw(self, amount):
        if not self.authenticated:
            raise Exception("User not authenticated. Please login first.")
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        if amount > self.balance:
            raise Exception("Insufficient funds.")
        self.balance -= amount
        return self.balance
                    
class MinimumBalanceAccount(BankAccount):
    def __init__(self, balance, username, password, minimum_balance=0):
        super().__init__(balance, username, password)
        self.minimum_balance = minimum_balance
    
    def withdraw(self, amount):
        if not self.authenticated:
            raise Exception("User not authenticated. Please login first.")
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if self.balance - amount < self.minimum_balance:
            raise Exception(f"Cannot withdraw. Balance cannot go below minimum balance of {self.minimum_balance}.")
        self.balance -= amount
        return self.balance       

bank_account1 = BankAccount("500000", "Shirubia", "Buff1luff12021")

#authentication 

if bank_account1.authenticate("Shirubia", "Buff1luff12021"):
    print("Authenticated successfully.")
else:
    print("Authentication failed.")    

# Deposit money
try:
    new_balance = bank_account1.deposit(500) # Pass integer amount
    print(f"Deposited successfully. New balance: {new_balance}")
except Exception as e:
    print(f"Deposit error: {e}")

# Withdraw money
try:
    new_balance = bank_account1.withdraw(200)  # Pass integer amount
    print(f"Withdrawn successfully. New balance: {new_balance}")
except Exception as e:
    print(f"Withdrawal error: {e}")

# MinimumBalanceAccount example
min_acc = MinimumBalanceAccount(1000, "Shirubia", "Buff1luff12021", minimum_balance=100)
min_acc.authenticate("user2", "pass456")

try:
    min_acc.withdraw(950)  # This should raise an exception due to minimum balance
except Exception as e:
    print(f"Minimum balance withdrawal error: {e}")
