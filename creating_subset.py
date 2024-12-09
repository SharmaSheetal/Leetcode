def create_subset(i, arr, data, combination, r):
    # Base case: If the size of the current combination equals r
    if len(data) == r:
        combination.append(data[:])  # Append a copy of data
        return

    # If we've processed all elements in arr
    if i >= len(arr):
        return

    # Include the current element and recurse
    data.append(arr[i])
    create_subset(i + 1, arr, data, combination, r)

    # Exclude the current element (backtrack) and recurse
    data.pop()
    create_subset(i + 1, arr, data, combination, r)


def get_combination(arr, r):
    combination = []  # To store all combinations
    create_subset(0, arr, [], combination, r)
    return combination


# Example usage
arr = [1, 2, 3, 4,5,6]
r = 2
result = get_combination(arr, r)
print("Combinations of size", r, ":", result)

"""
Time complexity: O(r. nCr)
Space Complexty:  O(r. nCr)
Efficient for small n and r
"""
def generate_subsets(arr, r):
    n = len(arr)
    subsets = []
    
    # Loop from 0 to 2^n - 1 (all possible combinations)
    for i in range(1 << n): #example if n=3 --> 1 <<3 1000--> 8-->2^3
        subset = []
        # Check each bit position
        for j in range(n): #i=0 for empty subset
            if i & (1 << j):  # If the j-th bit is set in i
                subset.append(arr[j])
        # Only add subsets of length r
        if len(subset) == r:
            subsets.append(subset)
    
    return subsets

"""
Time Complexity: O(n2^n)
The space complexity is O(nCr), which is the space needed to store all possible subsets of length r. The temporary space used in each iteration is O(r),but this is negligible compared to the space required to store the output.
"""
