#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # Use a list comprehension to replace the elements
    new_list = [replace if item == search else item for item in my_list]
    
    # Return the new list
    return new_list
