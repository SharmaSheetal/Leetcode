def reverseInGroups(arr, k):
    # If k is greater than or equal to the size of the array,
    # reverse the entire array at once
    if k >= len(arr):
        arr.reverse()
    else:
        # Iterate through the array in steps of size k
        for i in range(0, len(arr), k):
            # Reverse the subarray from index i to i+k (or the end of the array if remaining elements are less than k)
            arr[i:i+k] = reversed(arr[i:i+k])


"""
Time Complexity: O(N).
Auxiliary Space: O(1).
"""