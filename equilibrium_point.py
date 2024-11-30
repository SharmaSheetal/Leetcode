def equilibriumPoint(arr):
    # Calculate the total sum of all elements in the array
    total_sum = sum(arr)

    # Iterate through the array from the second element to the second-to-last element
    for i in range(1, len(arr) - 1):
        # Calculate the sum of elements to the left of the current index
        left_total = sum(arr[:i])

        # Check if the sum of elements to the left is equal to the sum of elements to the right
        if left_total == total_sum - left_total - arr[i]:
            return i + 1  # Return the index as a 1-based index

    # If no equilibrium point is found, return -1
    return -1
"""
Time Complexity: O(N^2)
Auxiliary Space: O(1)
"""


def equilibriumPoint(arr):
    # Start with pivot index as 1 (second element)
    pivot = 1

    # Initialize right_sum as the sum of all elements after the first element
    right_sum = sum(arr[1:])

    # Initialize left_sum as 0 (no elements to the left of the first element initially)
    left_sum = 0

    # Iterate until the left_sum equals right_sum or pivot reaches the second last element
    while left_sum != right_sum and pivot < len(arr) - 1:
        # Update left_sum by adding the element before the pivot
        left_sum += arr[pivot - 1]

        # Update right_sum by subtracting the current pivot element
        right_sum -= arr[pivot]

        # Move pivot to the next index
        pivot += 1

    # If left_sum equals right_sum, return the equilibrium index
    if left_sum == right_sum:
        return pivot

    # If no equilibrium point is found, return -1
    return -1
"""
Time Complexity: O(N)
Auxiliary Space: O(1)
"""