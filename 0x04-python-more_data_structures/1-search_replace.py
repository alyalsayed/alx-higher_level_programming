#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # Create a new list to store the modified values
    new_list = []
    
    # Iterate over the elements in the input list
    for item in my_list:
        # Replace the element if it matches the search value, otherwise add it to the new list
        if item == search:
            new_list.append(replace)
        else:
            new_list.append(item)
    
    # Return the new list
    return new_list
