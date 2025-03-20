from lab import *

def main():
    # Create a list of numbers from 1 to n
    n = int(input("Enter the number of elements for the list: "))
    num_list = create_list(n)
    print("List of numbers:", num_list)

    # Modify the list
    value_to_append = int(input("Enter a value to append to the list: "))
    value_to_insert = int(input("Enter a value to insert at the beginning of the list: "))
    value_to_remove = int(input("Enter a value to remove from the list: "))
    modify_list(num_list, value_to_append, value_to_insert, value_to_remove)
    print("Modified list:", num_list)

    # Slice the list
    start = int(input("Enter the starting index for slicing: "))
    end = int(input("Enter the ending index for slicing: "))
    sliced_list=slice_list(num_list, start, end)
    print("The sliced string is ",sliced_list)

if __name__ == "__main__":
    main()
