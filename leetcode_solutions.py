def two_sum(numbers: list[int], target: int) -> tuple[int, int]:
    """
    Description:
        Given a list of integers %numbers% and an integer %target%
        Returns a tuple of two indices of elements in a list whose sum equals the %target%
        If there is no solution, then returns a tuple of two zeros
    """

    indices_elements: list[tuple[int, int]] = list(enumerate(numbers)) # # Create a list of tuples containing original indices and their corresponding numbers
    indices_elements.sort(key=lambda x: x[1]) # Sort the list based on the numerical values
    
    # Use two pointers
    left: int =  0
    right: int = len(numbers) - 1
    while left < right:

        current_sum: int = indices_elements[left][1] + indices_elements[right][1]
        #  Calculate the sum of the numbers at the current pointers
        if current_sum < target:
            left += 1
        elif target < current_sum:
            right -= 1
        else: # If the sum equals the target, return the original indices of these elements
            return (indices_elements[left][0], indices_elements[right][0])
    return (0, 0) # No solution

def search_insert_position(lst: list[object], target: object) -> int:
    """
    Description:
        Given a sorted list %lst% and a value %target%
        Returns the index of %target% in %lst% if it exists
        Otherwise, returns the index where <target> would theoretically be inserted to maintain sorted order

    Note:
        The objects in %lst% and %target% must support the '<' operator.
    """
    left: int = 0
    right: int = len(lst)
    # left and right are pointers to elements in the vector on both sides

    while left < right: # We will consider the range [left; right)
        # Using an open interval is not necessary, since Python integers do not overflow
        # We can safely use either while 'left < right' with 'right = middle' or while 'left <= right' with 'right = middle - 1'

        middle: int = (left + right) // 2

        # For convenience, only the operator<() will be used
		# We shift the left and right pointers
        if lst[middle] < target:
            left = middle + 1
        elif target < lst[middle]:
            right = middle
        else:
            return middle # Found target
    return left # Returns the index in the list where the target would theoretically be positioned 


def binary_search(lst: list[object], target: object) -> int:
    """
    Description:
        Given a sorted list %lst% and a value %target%
        Returns the index of %target% in %lst% if it exists
        Otherwise, returns -1

    Note:
        The objects in %lst% and %target% must support the '<' operator.
    """
    left: int = 0
    right: int = len(lst)
    # left and right are pointers to elements in the vector on both sides

    while left < right: # We will consider the range [left; right)
        # Using an open interval is not necessary, since Python integers do not overflow
        # We can safely use either while 'left < right' with 'right = middle' or while 'left <= right' with 'right = middle - 1'

        middle: int = (left + right) // 2

        # For convenience, only the operator<() will be used
		# We shift the left and right pointers
        if lst[middle] < target:
            left = middle + 1
        elif target < lst[middle]:
            right = middle
        else:
            return middle # Found target
    return -1 # Returns the index in the list where the target would theoretically be positioned 

def sign(number: int) -> int:
    if number > 0:
        return 1
    elif number < 0:
        return -1
    else:
        return 0

def reversed(number: int) -> int:
    """
    Given an interger %number%
    Returns the reversed number
    """
    return sign(number)*int(str(abs(number))[::-1])