def create_list(n):
    """
    Instead of returning 0, this method should Create a list of numbers from 1 to n and return it.

    :param n: The number of elements in the list.
    :return: The created list.

    Instructions:
    --------------
    1. Use the `range()` function to generate a list of numbers from 1 to `n`.
    2. Ensure that the function handles the case when `n` is 0 or negative.
    """
    if n <= 0:
        raise ValueError("Number of elements must be positive")
    return list(range(1,n+1))

def modify_list(my_list, value_to_append=None, value_to_insert=None, value_to_remove=None):
    """
    Modify the list by appending, inserting, and removing elements.

    :param my_list: The list to modify.
    :param value_to_append: The value to append to the list (default is None).
    :param value_to_insert: The value to insert at the beginning of the list (default is None).
    :param value_to_remove: The value to remove from the list (default is None).
    """
    if value_to_append is not None:
        # Write your code here to append the value to the list.
    
    if value_to_insert is not None:
        # Write your code here to insert the element in the beginning of the list
            
    if value_to_remove is not None:
        # Write your code here to remove the element from the list.

def slice_list(my_list, start=0, end=3):
    """
   Instead of returning 0 this method should Slice the list and return the sliced string.

    :param my_list: The list to slice.
    :param start: The starting index for slicing (default is 0).
    :param end: The ending index for slicing (default is 3).
    """
    # Write your code here
    return 0

