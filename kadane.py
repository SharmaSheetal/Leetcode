def maxSubArraySum(self, arr):
    # Initialize max_sum and s to negative infinity, 
    # since we want to ensure any sum found in the array will be larger initially
    max_sum, s = float('-inf'), float('-inf')
    
    # Iterate through each element of the array
    for i in range(len(arr)):
        # For each element, decide whether to include the current element in the previous subarray 
        # (i.e., s + arr[i]) or start a new subarray (i.e., arr[i])
        s = max(arr[i], s + arr[i])
        
        # Update the maximum sum found so far
        max_sum = max(s, max_sum)
    
    # Return the maximum sum found for any subarray
    return max_sum

"""
Time Complexity: O(n)
Space Complexity: O(1)

"""