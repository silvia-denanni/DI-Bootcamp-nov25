#Challenge 1: Letter Index Dictionary 

#Create a dictionary that stores the indices (number of the position) of each letter 
#in a word provided by the user(input()).
#review each char in str
#for each, pay attention to index and what char
#check it against what is already in the dictionary's key
#if char in dict:
  #add index to char's list
#else, made new dict key value pair
#char = key, index = value


user_word = input("enter a word: ")        
my_dictionary = {}                     # Initialize an empty dictionary to store characters and their indices
for index, char in enumerate(user_word):   # Loop through each character and its index in the word inputted by the user
            # Take the first item of the dictionary pair and call it "index" (the position of the character in the word)
            # Take the second item of the pair and call it "char" (the character itself)
    if char in my_dictionary:
      my_dictionary[char].append(index)             # If yes, append the current index to the existing list
    else:
       my_dictionary[char] = [index]  #If no, create a new key with the character and start a list with the current index
print(my_dictionary)


# Challenge 2: Affordable Items
# Create a program that prints a list of items that can be purchased with a given amount of money.
# You will be provided with a dictionary (items_purchase) where the keys are the item names and the values are their prices 
# The priority is defined by the position of the iten on the dictionary: from the most important to the less important.
# You will also be given a string (wallet) representing the amount of money you have.
# CLEANING
# 1) You need to clean the dollar sign and the commas using python. Don’t hard code it.
# DETERMINING AFFORDABLE
# 2)Create a list called "Basket" and add there the items that you can buy with the money you have on the wallet
# 3)Don’t forget to update the wallet after buying an item.
# 4)If the basket is empty (no items can be afforded), return the string “Nothing”.
# 5)If the basket is not empty, print the basket list in alphabetical order.

#CLEAN DICTIONARY
items_purchase_dirty = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
items_purchase = {}
for item, price in items_purchase_dirty.items():     #we need both key and value because the basket will receive both key and  item
   new_price = int(price.replace("$", "").replace(",", ""))
   items_purchase[item] = (new_price)  
  
print(items_purchase)

#CLEAN VARIABLE

dirty_wallet = "$300"
wallet = int(dirty_wallet.replace("$",""))
print(wallet)                   

# Affordable Items Program NUMBER 1
items_purchase = {'Water': 1, 'Bread': 3, 'TV': 1000, 'Fertilizer': 20}
wallet = "300"
wallet_amount = int(wallet) # This is needed to trasform the string in an integer
basket = [] #empty list to be filled

for item, price in items_purchase.items():  #for loop with .items function to access both key and value
   if price <= wallet_amount: #if the dictionary value is lower than the budget
      basket.append(item)  #append the item to the basket
      wallet_amount -= price  # here we subtract from the wallet the purchase

#LESS ELEGANT BUT OK FOR LEVEL WAY
if basket: 
   print(sorted(basket))
else:
   print("nothing")

#MORE ELEGANT WAY

if not basket:     #if the basket is empty
   print("Nothing")
else:
   print(sorted(basket))   #print the basket items in alphabetical order
      
# Affordable Items Program NUMBER 2
dirty_items_purchase = {"Apple": "$4", "Honey": "$3", "Fan": "$14", "Bananas": "$4", "Pan": "$100", "Spoon": "$2"}
dirty_wallet = "$100"

#CLEAN DICTIONARY
dirty_items_purchase = {"Apple": "$4", "Honey": "$3", "Fan": "$14", "Bananas": "$4", "Pan": "$100", "Spoon": "$2"}
items_purchase = {}
for key, value in dirty_items_purchase.items():
   value.replace("$","").replace(",","")
   items_purchase[item] = int(key)

print(items_purchase)

  
#CLEAN WALLET
dirty_wallet = "$100"
wallet = int(dirty_wallet.replace("$","").replace(",",""))
print(wallet) 

# Affordable Items
basket = []
for item, price in items_purchase.items():
   if wallet > price:
      basket.append(item)
      wallet -= price
      
if not basket:     
   print("Nothing")
else:
   print(sorted(basket)) 

