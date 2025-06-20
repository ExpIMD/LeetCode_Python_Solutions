def two_sum(numbers: list[int], target: int) -> tuple[int, int]:
    """
    Given a list of integers %numbers% and an integer %target%
    Returns a tuple of two indices of elements in a vector whose sum equals the %target%
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