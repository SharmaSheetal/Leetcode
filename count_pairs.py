
def countPairs(self, arr, brr):
    c = 0  # Initialize the count of valid pairs

    # Iterate over each element `i` in `arr`
    for i in arr:
        # Iterate over each element `j` in `brr`
        for j in brr:
            # Check the condition if `i^j > j^i`
            if i**j > j**i:
                c += 1  # Increment the count if the condition is true

    return c  
"""
Time Complexity: O(NM)
Auxiliary Space: O(1)
"""
def countPairs(self, arr, brr):
    # Helper function to find the index to insert `x` in `brr` using binary search.
    def binary_serach_right_index(a, x):
        lo, hi = 0, len(a)
        while lo < hi:
            mid = (lo + hi) // 2
            if x < a[mid]: 
                hi = mid  # Move `hi` to the left of `mid`
            else: 
                lo = mid + 1  # Move `lo` to the right of `mid`
        return lo  # Return the index where `x` should be inserted

    # Main counting function that calculates the number of pairs for a given `x`.
    def count(x, brr, brr_count):
        c = 0  # Initialize count of pairs

        # Special case for `x = 0`: There are no pairs with `x = 0` that satisfy the condition.
        if x == 0:
            return 0
        # Special case for `x = 1`: Count the number of `1`s in `brr`.
        elif x == 1:
            return brr_count[0]
        else:
            # Add the number of pairs where `x > y` and `y < 2` (i.e., `y = 0 or 1`).
            c += brr_count[0] + brr_count[1]

            # Find the first index in `brr` where the element is greater than `x`.
            idx = binary_serach_right_index(brr, x)

            # Count the number of elements in `brr` greater than `x`.
            c += len(brr) - idx

            # Special cases for `x = 2` and `x = 3` based on specific problem constraints.
            if x == 2:
                c -= brr_count[3] + brr_count[4]  # Subtract counts for `y = 3, 4`
            elif x == 3:
                c += brr_count[2]  # Add count for `y = 2`

        return c  # Return the total count of valid pairs for `x`

    num_of_pairs = 0  # Initialize the total number of pairs found.
    brr.sort()  # Sort `brr` to enable binary search.

    # Count the occurrences of numbers less than 5 in `brr`.
    brr_count = [0] * 5
    for y in brr:
        if y < 5:
            brr_count[y] += 1  # Increment the count of occurrences for `y`

    # Iterate through each element `x` in `arr` and count valid pairs.
    for x in arr:
        num_of_pairs += count(x, brr, brr_count)

    return num_of_pairs  
"""
Time Complexity: O((N + M)log(N))  --> len(brr)--N
Auxiliary Space: O(1)
"""