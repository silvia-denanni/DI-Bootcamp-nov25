#1
#You are given two lists. Convert them into a dictionary where the first list contains the keys and the second list contains the corresponding values. Expected output -->{'Ten': 10, 'Twenty': 20, 'Thirty': 30}

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
my_dict = dict(zip(keys, values))
print(my_dict)

#2
#Write a program that calculates the total cost of movie tickets for a family based on their ages.
# Family members’ ages are stored in a dictionary.
# The ticket pricing rules are as follows:
# Under 3 years old: Free
# 3 to 12 years old: $10
# Over 12 years old: $15
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
# Loop through the family dictionary to calculate the total cost.
# Print the ticket price for each family member.
# Print the total cost at the end.

#3
#Create and manipulate a dictionary that contains information about the Zara brand. 
# Create a dictionary called brand with the provided data.
# Modify and access the dictionary as follows:
# Change the value of number_stores to 2.
# Print a sentence describing Zara’s clients using the type_of_clothes key.
# Add a new key country_creation with the value Spain.
# Delete the creation_date key.
# Print the last item in international_competitors.
# Print the major colors in the US.
# Print the number of keys in the dictionary.
# Print all keys of the dictionary.
# Check if international_competitors exists and, if so, add “Desigual” to the list.

brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]
    }
}
# brand["number_stores"] = 2
# print(brand)
# print(f"Zara offers clothes and products for {', '.join(brand['type_of_clothes'])}.")
# brand["country_creation"] = "Spain"
# print(brand)
# del brand["creation_date"]
# print(brand)
# print(brand["international_competitors"][-1])
# print(brand["major_color"]["US"])
# print(len(brand))
# print(brand)
# if "international_competitors" in brand:
#     brand["international_competitors"].append("Desigual")
#     print(brand["international_competitors"])
# more_on_zara = {
#    "creation_date": 1975,
#    "number_stores": 7000
#    }
# brand.update(more_on_zara)
# print(brand)

#4 You are given a list of Disney characters. Create three dictionaries based on different patterns as shown below:
# 1. Create a dictionary that maps characters to their indices:
# 2. Create a dictionary that maps indices to characters:
# 3. Create a dictionary where characters are sorted alphabetically and mapped to their indices:

users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
# index = [0,1,2,3,4]
# users_index = dict(zip(users,index))
# print(users_index)    FINIRE
