def countTriplet(arr):
    # Iterate over the array from the end, considering each element as the sum
    i=len(arr)-1
    c=0
    # Sort the array to use the two-pointer technique
    arr.sort()
    while i >= 0:
        # Initialize two pointers
        j, k = 0, i - 1  # `j` starts from the beginning, `k` starts just before `i`
        
        # Use two pointers to find pairs whose sum equals arr[i]
        while j < k:
            # Check the sum of arr[j] and arr[k]
            if arr[j] + arr[k] > arr[i]:
                # If the sum is greater, move the `k` pointer left to reduce the sum
                k -= 1
            elif arr[j] + arr[k] < arr[i]:
                # If the sum is smaller, move the `j` pointer right to increase the sum
                j += 1
            else:
                # If a pair is found, increment the triplet count
                c += 1
                
                # Move both pointers to look for other pairs
                j += 1
                k -= 1
        
        # Move to the next element in the array to consider it as the sum
        i -= 1
    
    # Return the total count of triplets
    return c
"""
Time Complexity: O(N2), As we are sorting the array for which the complexity is O(NlogN) and running a loop of size N2, So the total complexity becomes O(NlogN+N2) ~ O(N2).
Space Complexity: O(1), As we are using constant extra space.

"""

# Other Approach
def countTriplets(arr, n):
    freq = [0 for i in range(100)]
     
    # Loop to count the frequency
    for i in range(n):
        freq[arr[i]] += 1
    count = 0
     
    # Loop to count for triplets
    for i in range(n):
        for j in range(i + 1, n, 1):
            if(freq[arr[i] + arr[j]]):
                count += 1
    return count
"""
Time Complexity: O(N2).
Auxiliary Space: O(N).
"""

def countTriplet(arr):
        c=0
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                if arr[i]+arr[j] in arr:
                    c+=1
        return c

"""
Time Complexity: O(N3).
Auxiliary Space: O(1).
"""