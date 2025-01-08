def access_list_element(my_list, index):
    try:
        # Attempt to access the list at the given index
        print(f"The element at index {index} is: {my_list[index]}")
    except IndexError:
        # Handle the case where the index is out of range
        print(f"Error: The index {index} is out of range for the list.")

# Main program
def main():
    my_list = [10, 20, 30, 40, 50]
    
    # Test with a valid index
    access_list_element(my_list, 2)  # Valid index
    
    # Test with an invalid index
    access_list_element(my_list, 10)  

if __name__ == "__main__":
    main()
x