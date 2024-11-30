def leaders(arr):
    result = []  # Initialize an empty list to store leader elements
    n = len(arr)  # Get the length of the array
    current_max = arr[-1]  # Start with the last element as the current maximum

    # Traverse the array from right to left
    for i in range(n - 1, -1, -1):
        # Check if the current element is greater than or equal to the current max
        if arr[i] >= current_max:
            result.append(arr[i])  # Add it to the result list as it is a leader
            current_max = arr[i]  # Update the current max

    # Reverse the result list as we traversed the array from right to left
    result.reverse()

    return result  

"""
Time Complexity: O(N).
Auxiliary Space: O(n).
"""