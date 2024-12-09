def findTwoElements(arr): 
    # Initialize variables for missing and repeating numbers
    missing_number, repeating_number = 0, 0

    # Create a frequency array to count occurrences of each number
    # Size is len(arr) + 1 to account for numbers from 1 to len(arr)
    frequency = [0] * (len(arr) + 1)

    # Populate the frequency array
    for num in arr:
        frequency[num] += 1

    # Traverse the frequency array to find missing and repeating numbers
    for i in range(1, len(frequency)):  # Start from 1 as numbers range from 1 to len(arr)
        if frequency[i] == 0:  # Missing number will have a frequency of 0
            missing_number = i
        elif frequency[i] == 2:  # Repeating number will have a frequency of 2
            repeating_number = i

    # Return the results as [repeating_number, missing_number]
    return [repeating_number, missing_number]
"""
Time Complexity: O(N).
Auxiliary Space: O(N).
"""

def findTwoElements(arr):
    # Length of the array
    n = len(arr)
    
    # Compute the sum and sum of squares for numbers from 1 to n
    sum_n = (n * (n + 1)) // 2  # Sum of first n natural numbers
    sum_n_square = (n * (n + 1) * (2 * n + 1)) // 6  # Sum of squares of first n natural numbers
    
    # Compute the actual sum and sum of squares from the array
    actual_sum = sum(arr)
    actual_sum_square = sum(x * x for x in arr)
    
    # Equation 1: (x - y)
    diff_sum = sum_n - actual_sum  # x - y
    
    # Equation 2: (x^2 - y^2) = (x - y)(x + y)
    diff_square_sum = sum_n_square - actual_sum_square  # x^2 - y^2
    
    # Compute (x + y) using (x^2 - y^2) / (x - y)
    sum_xy = diff_square_sum // diff_sum  # x + y
    
    # Solve for x (missing number) and y (repeating number)
    missing_number = (diff_sum + sum_xy) // 2  # x
    repeating_number = (sum_xy - diff_sum) // 2  # y
    
    return [repeating_number, missing_number]

"""
Time Complexity: O(N).
Auxiliary Space: O(1).
"""

#XOR

def find_missing_and_repeating(arr):
    # Step 1: Calculate XOR of all array elements and numbers from 1 to n
    xor_result = 0
    n = len(arr)
    
    for i in range(n):
        xor_result ^= arr[i]  # XOR all elements in the array
        xor_result ^= (i + 1)  # XOR with numbers from 1 to n
    
    # Step 2: Find the rightmost set bit in xor_result
    rightmost_set_bit = xor_result & -xor_result  # Isolate the rightmost set bit

    # Step 3: Divide numbers into two groups based on the rightmost set bit
    group_with_bit_set = 0
    group_without_bit_set = 0
    
    for i in range(n):
        # Group numbers in the array
        if arr[i] & rightmost_set_bit:
            group_with_bit_set ^= arr[i]
        else:
            group_without_bit_set ^= arr[i]
        
        # Group numbers from 1 to n
        if (i + 1) & rightmost_set_bit:
            group_with_bit_set ^= (i + 1)
        else:
            group_without_bit_set ^= (i + 1)

    # Step 4: Determine which number is missing and which is repeating
    if group_with_bit_set in arr:
        repeating_number = group_with_bit_set
        missing_number = group_without_bit_set
    else:
        repeating_number = group_without_bit_set
        missing_number = group_with_bit_set

    return [repeating_number, missing_number]

"""
Time Complexity: O(N).
Auxiliary Space: O(1).
"""

bit_no = 0  # To store the bit position
while (xor & (1 << bit_no)):  # Check if the bit at position 'bit_no' is 0
    bit_no += 1
set_bit = bit_no  # `set_bit` will contain the position of the rightmost unset bit

# and while dividing
arr[i] & (1<<set_bit )
i+1 & (1<<set_bit)