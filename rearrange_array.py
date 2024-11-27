def rearrange(arr, n):
    # If there is only one element, no rearrangement is needed
    if n != 1:
        j = n - 1  # Pointer to the last element in the array

        # Iterate over even indices (0, 2, 4, ...)
        for i in range(0, n, 2):
            k = n - 1  # Start at the last element for shifting
            temp = arr[j]  # Store the current largest element to be placed at index i

            # Shift all elements from the current position (i) to the end (k) by one position
            while k >= i:
                arr[k] = arr[k - 1]  # Shift the element at position k-1 to position k
                k -= 1  # Move to the next position towards the left

            # Place the largest element stored in `temp` at index `i`
            arr[i] = temp

            # Decrement the pointer `j` to point to the next largest element
            j -= 1
"""
Time Complexity: O(N2).
Auxiliary Space: O(1).
"""

def rearrange(arr, n):
    # Pointers for the largest and smallest elements
    max_idx = n - 1
    min_idx = 0
    
    # Placeholder for result array
    result = [0] * n
    
    # Fill even indices with max elements and odd indices with min elements
    for i in range(n):
        if i % 2 == 0:  # Even index: Place the largest remaining element
            result[i] = arr[max_idx]
            max_idx -= 1
        else:  # Odd index: Place the smallest remaining element
            result[i] = arr[min_idx]
            min_idx += 1
    
    # Copy result back to the original array
    for i in range(n):
        arr[i] = result[i]

"""
Time Complexity: O(N).
Auxiliary Space: O(N).
"""

def rearrange(arr, n):
    # Initialize pointers for the smallest and largest elements
    min_ = 0  # Points to the smallest element
    max_ = n - 1  # Points to the largest element

    # Determine a value greater than the largest element in the array
    max_element = arr[-1] + 1  # This ensures we can encode two values in one index

    # First pass: Encode both the current element and the new element at each position
    for i in range(n):
        if i % 2 == 0:
            # For even indices, place the largest available element
            arr[i] += ((arr[max_] % max_element) * max_element)
            max_ -= 1  # Move to the next largest element
        else:
            # For odd indices, place the smallest available element
            arr[i] += ((arr[min_] % max_element) * max_element)
            min_ += 1  # Move to the next smallest element

    # Second pass: Decode the new values to finalize the rearranged array
    for i in range(n):
        arr[i] = arr[i] // max_element  # Extract the new encoded value

"""
Time Complexity: O(N).
Auxiliary Space: O(1).
"""