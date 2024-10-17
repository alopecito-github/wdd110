# Example 4
def main():
    # Count from zero to nine by one.
    for i in range(10):
        print(i)
    print()
    # Count from five to nine by one.
    for i in range(5, 10):
        print(i)
    print()
    # Count from zero to eight by two.
    for i in range(0, 10, 2):
        print(i)
    print()
    # Count from 100 down to 70 by three.
    for i in range(100, 69, -3):
        print(i)


    print ("*************Example 5***************")

    # Create a list of color names.
    colors = ["red", "orange", "yellow", "green", "blue"]
    # Use a for loop to print each element in the list.
    for color in colors:
        print(color)
    print()
    # Use a different for loop to
    # print each element in the list.
    for i in range(len(colors)):
        # Use the index i to retrieve
        # an element from the list.
        color = colors[i]
        print(color)

    print ("*************Example 6 Break***************")

    
    sum = 0
    # Get ten or fewer numbers from the user and
    # add them together.
    for i in range(10):
        number = float(input("Please enter a number: "))
        if number == 0:
            break
        sum += number
    # Print the sum of the numbers for the user to see.

    print(f"sum: {sum}")
    
    
    print ("*************Example 7 While Loop***************")
    list1 = ["red", "orange", "yellow", "green", "blue"]
    list2 = ["red", "orange", "green", "green", "blue"]
    index = compare_lists(list1, list2)
    if index == -1:
        print("The contents of list1 and list2 are equal")
    else:
        print(f"list1 and list2 differ at index {index}")
        
def compare_lists(list1, list2):
    """Compare the contents of two lists. If the contents
    of the two lists are not equal, return the index of
    the first difference. If the contents of the two lists
    are equal, return -1.
    Parameters
        list1: a list
        list2: another list
    Return: an index or -1
    """
    # Get the length of the shortest list.
    length1 = len(list1)
    length2 = len(list2)
    limit = min(length1, length2)
    # Begin at the first index (0) and repeat until the
    # computer finds two elements that are not equal or
    # until the computer reaches the end of the shortest
    # list, whichever comes first.
    i = 0
    while i < limit:
        # Retrieve one element from each list.
        element1 = list1[i]
        element2 = list2[i]
        # If the two elements are not
        # equal, quit the while loop.
        if element1 != element2:
            break
        # Add one to the index variable.
        i += 1
    # If the length of both lists are equal and the
    # computer verified that all elements are equal,
    # set i to -1 to indicate that the contents of
    # the two lists are equal.
    if length1 == length2 == i:
        i = -1
    return i






# Call main to start this program.
if __name__ == "__main__":
    main()