import typing

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
    """
    Sign math function  
    If the number is positive, it returns 1     
    If the number is negative, it returns -1    
    Otherwise, it returns 0
    """
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

def last_word_length(line: str) -> int:
    """
    Given a string %line%   
    Returns the length of the last word in %line%
    """
    end: int = len(line) - 1

    while end >= 0 and line[end] == " ":
        end -= 1

    start = end
    # Instead of using a variable length, we declare start to avoid unnecessary calculations
        
    while start >= 0 and line[start] != " ":
        start -= 1

    return end - start # Using split is inefficient because this method processes the entire string, not just its last word
    # return len(line.split()[-1])


def Boyer_Moore_vote_algorithm(collection: typing.Iterable[object]) -> object:
    """
    Given a collection <col>
    Returns the element that occurs more than half of the time in the collection (the majority element)
    If there is no majority element, a random element is returned
    """

    """
    It works by maintaining a candidate and a counter:
    it increments the counter when the current element matches the candidate, decrements otherwise,
    and resets the candidate when the counter reaches zero.
    After one pass, the candidate is the majority element if one exists.
    """
    candidate: object = None
    frequence: int = 0
    for x in collection:
        if frequence == 0:
            candidate = x
        if x == candidate:
            frequence += 1
        else:
            frequence -= 1
    return candidate

def majority_element(collection: typing.Iterable[object]) -> object:
    """
    Given a collection <collection>
    Returns the element that occurs more than half of the time in the collection (the majority element)
    If there is no majority element, returns None
    """
    mapping = {}
    times: int = len(collection) / 2

    for x in collection:
        mapping[x] += 1
        if mapping[x] > times:
            return x
        
    return None

def is_palindrome(number: int) -> bool:
    if number < 0: return False
    return reversed(number) == number

