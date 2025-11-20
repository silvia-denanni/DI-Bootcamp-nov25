import math

# Create a Pagination class that simulates a basic pagination system

# Step 1: Create the Pagination Class to represent paginated content
# Step 2: Implement the __init__ Method
# Step 3: Implement the get_visible_items() Method


class Pagination():
    def __init__(self, items = None, page_size = 10):
        if items is None:
            items = []
        self.items = items
        self.page_size = page_size
        self.current_index = 0
        self.total_pages = math.ceil(len(self.items) / self.page_size)   #It divides the total number of items
                                                    #by the page size and rounds up to make sure all items fit

    def get_visible_items(self):
        start = self.current_index * self.page_size  #starting position= current page number * n items in page 
        end = start + self.page_size            #ending position = starting position + page size
        return self.items[start:end]            #returns the slice of the list from start to end
    
    def go_to_page(self, page_num):
        if page_num < 1 or page_num > self.total_pages:
            raise ValueError ("Invalid page number")
        self.current_index = page_num -1  #because pages are counted from 1 for users 
        
    def first_page(self):
        self.current_index = 0
        return self
    
    def last_page(self):
        self.current_index = self.total_pages - 1   # minus 1 because of zero-based indexing
        return self
    
    def next_page(self):
       if self.current_index < self.total_pages - 1:  # minus 1 because of zero-based indexing
            self.current_index += 1
            return self
       
    def previous_page(self):
       if self.current_index > 0:
            self.current_index -= 1                  # minus 1 because of zero-based indexing
            return self

# All navigation methods (except go_to_page) should return self to allow method chaining

alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)

print(p.get_visible_items())
# ['a', 'b', 'c', 'd']

p.next_page()
print(p.get_visible_items())
# ['e', 'f', 'g', 'h']

p.last_page()
print(p.get_visible_items())
# ['y', 'z']

p.go_to_page(10)
print(p.current_current_index + 1)
# Output: ValueError

p.go_to_page(0)
# Raises ValueError