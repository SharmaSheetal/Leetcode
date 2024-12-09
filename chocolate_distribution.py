def findMinDiff(self, arr, M):
    # Step 1: Sort the input array.
    # Sorting ensures that elements within any subarray of size M 
    # are contiguous in terms of their values, reducing unnecessary comparisons.
    arr.sort()

    # Step 2: Initialize the variable to store the minimum difference.
    # Start with infinity since we want to find the minimum difference.
    current_difference = float('inf')

    # Step 3: Initialize two pointers for the sliding window.
    # i: start of the window, j: end of the window.
    i = 0
    j = M - 1  # The subarray size is M, so j starts at M-1.

    # Step 4: Slide the window across the array.
    while j < len(arr):
        # Calculate the difference between the maximum and minimum 
        # of the current subarray.
        current_difference = min(current_difference, arr[j] - arr[i])

        # Move the window one step forward.
        i += 1
        j += 1

    # Step 5: Return the minimum difference found.
    return current_difference

"""
Time Complexity:O(nlogn)   
Space Complexity: O(1) 

"""