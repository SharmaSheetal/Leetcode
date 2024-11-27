def missingNumber(arr):
    # Calculate the total number of elements (n) that should be in the array,
    # including the missing number.
    n = len(arr) + 1

    # Calculate the sum of the first n natural numbers using the formula:
    # sum_total = n * (n + 1) / 2
    sum_total = (n * (n + 1)) // 2

    # Subtract the sum of the elements in the given array from the total sum
    # to find the missing number.
    return sum_total - sum(arr)

"""
Time Complexity: O(n), As in this we are iterating the array.
Space complexity : O(1), As we only use the constant extra space
"""