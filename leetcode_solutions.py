import typing

def two_sum(numbers: list[int], target: int) -> tuple[int, int]:
    """
    Description:
        Given a list of integers \<numbers\> and an integer \<target\>
        Returns a tuple of two indices of elements in a list whose sum equals the \<target\>
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
        Given a sorted list \<lst\> and a value \<target\>
        Returns the index of \<target\> in \<lst\> if it exists
        Otherwise, returns the index where <target> would theoretically be inserted to maintain sorted order

    Note:
        The objects in \<lst\> and \<target\> must support the '<' operator.
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
        Given a sorted list \<lst\> and a value \<target\>
        Returns the index of \<target\> in \<lst\> if it exists
        Otherwise, returns -1

    Note:
        The objects in \<lst\> and \<target\> must support the '<' operator.
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
    Description:
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
    Description:
        Given an interger \<number\>  
        Returns the reversed \<number\>
    """
    return sign(number)*int(str(abs(number))[::-1])

def last_word_length(line: str) -> int:
    """
    Description:
        Given a string \<line\>
        Returns the length of the last word in \<line\>
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
    Description:
        Given a collection \<collection\>
        Returns the element that occurs more than half of the time in the \<collection\> (the majority element)
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
    Description:
        Given a collection \<collection\>
        Returns the element that occurs more than half of the time in the \<collection\> (the majority element)
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
    """
    Description:
        Given an integer \<number\>
        Checks if the \<number\> is a palindrome
    """
    if number < 0: return False
    return reversed(number) == number

def is_palindrome(line: str) -> bool:
    """
    Description:
        Given a string \<line\>
        Checks if the \<line\> is a palindrome
    """

    if not line: # We will consider the empty string as a palindrome
        return True

    left, right = 0, len(line) - 1 # Initialize two pointers: one at the start and one at the end of the string

    while left < right:
        if not line[left].isalnum(): # If the character at 'left' is not alphanumeric, skip it
            left += 1
            continue
        if not line[right].isalnum(): # If the character at 'right' is not alphanumeric, skip it
            right -= 1
            continue
        if line[left].lower() != line[right].lower(): # Characters do not match, not a palindrome
            return False
        # Characters match; move inward towards the center
        left += 1
        right -= 1

    return True

    """
    This solution is the shortest, but not efficient in terms of time or memory.
    
    filtered = "".join(ch.lower() for ch in s if ch.isalnum())
    return filtered == filtered[::-1]

    """

def Pascal_triangle(rows_count: int) -> list[list[int]]:
    """
    Description:
        Given an integer \<rows_count\>
        Returns Pascal's triangle with \<rows_count\> rows
    """

    result: list[list[int]]  = [] # Initialize the Pascal triangle

    for i in range(rows_count):
        result.append([1] * (i + 1)) # All elements are set to 1 by default to avoid having to specify additional conditions
        for j in range(1, i):
            result[i][j] = result[i-1][j] + result[i-1][j-1] # Element storage rule

    return result

def get_Pascal_triangle_row(row_index: int) -> list[int]:
    """
    Description:
        Given an integer \<row_index\>
        Returns Pascal's triangle row with \<row_index\> index
    """

    row: list[int] = [1] * (row_index + 1) # Initialize the Pascal triangle row

    # Compute the internal elements of the row (excluding the edges)
	# Update elements from right to left to avoid overwriting values that are still needed for calculations
    for i in range(1, row_index):
        for j in range(i, 0, -1):
            row[j] += row[j-1]
    return row

def minimum_triangle_total(triangle = list[list[int]]) -> int:
    """
    Description:
        Given a list \<triangle\>
        For each step, you may move to an adjacent number of the row below.
        More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row
        Returns the minimum path sum from top to bottom
    """

    rows_count: int = len(triangle)
    min_sums: list[int] = triangle[-1].copy()

    for i in range(rows_count - 2, -1, -1):
        for j in range(i + 1):
            min_sums[j] = min(min_sums[j+1], min_sums[j]) + triangle[i][j]
    return min_sums[0]


def longest_common_prefix_sort(lines: list[str]) -> str:
    """
    Description:
        Given a list of strings \<lines\>.
        Returns the longest common prefix of all strings in the list.
        If there is no common prefix or the list is empty, returns an empty string "".
    Note:
        The solution uses lexicographical sorting
    """

    if len(lines) == 0:
        return ""
    
    # Sort the list lexicographically
    # After sorting, the strings with similar prefixes will be grouped together
    lines.sort()
    k = min(lines[0], lines[-1])

    # Compare characters of the first and last strings to find the common prefix
    for i in range(k):
        if lines[0][i] != lines[-1][i]:
            return lines[0][:i] # Return the prefix up to the point where mismatch occurs
    
    return lines[0][:k] # # If no mismatch found, entire shortest string is a common prefix

def longest_common_prefix_char_comparison(lines: list[str]) -> str:
    """
    Description:
        Given a list of strings \<lines\>.
        Returns the longest common prefix of all strings in the list.
        If there is no common prefix or the list is empty, returns an empty string "".
    Note:
        The solution compares all the strings in the list character by character
    """
    
    if len(lines) == 0:
        return ""
    
    prefix = lines[0] # Let's assume that the first line is the desired prefix
    for i in range(1, len(lines)): # Iterate through each subsequent string in the list
        k = min(len(prefix), len(lines[i]))

        for j in range(k): # Compare characters one by one to find where they differ
            if prefix[j] != lines[i][j]:
                k = j # Mismatch found, update k to current position j
                break

        prefix = lines[i][:k] # Update prefix to be only the common part with current string
        
        if not prefix: # If at any point, prefix becomes empty, no need to continue further
            break
                
    return prefix