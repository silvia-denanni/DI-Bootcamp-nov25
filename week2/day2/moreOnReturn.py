# Practical Examples
# A. Variable Assignment and Reuse 

def sum_list_with_return(lst):
    return sum(x for x in lst if isinstance(x, int))

def sum_list_with_print(lst):
    print(sum(x for x in lst if isinstance(x, int)))

# Using return                                       Only version lets you use the result in further calculations
result = sum_list_with_return([1, 2, 3, 'a', 4])
print("Returned value:", result)  # Output: Returned value: 10
print(result * 2)                 # Output: 20

# Using print
result = sum_list_with_print([1, 2, 3, 'a', 4])  # Output: 10
print("Returned value:", result)  # Output: Returned value: None
# result * 2 would cause an error!



def double_sum(lst):
    return 2 * sum_list_with_return(lst)

print(double_sum([1, 2, 3]))  #>>> 12       This is impossible with the print version, since it returns "None"


lists = [[1, 2, 3], [4, 5, 6], [100, 200, 300]]
totals = [sum_list_with_return(lst) for lst in lists]
print("Total of all sums:", sum(totals))  #>>> 621   This is impossible with the print version, since it returns "None"
