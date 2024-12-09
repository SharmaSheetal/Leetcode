def checkTriplet(arr):
    # Square each element in the array to work with squares directly
    arr = [i * i for i in arr]
    
    # Sort the array to enable the two-pointer technique
    arr.sort()
    
    # Iterate from the largest element (last index) down to the third element
    for k in range(len(arr) - 1, 1, -1):  # Loop starts at the last element
        j = k - 1  # Initialize `j` as the second last element
        i = 0      # Initialize `i` as the first element
        
        # Use the two-pointer technique to find a pair that sums to `arr[k]`
        while i < j:
            if arr[j] + arr[i] == arr[k]:  # Check if the sum of `arr[i]` and `arr[j]` equals `arr[k]`
                return True  # A Pythagorean triplet is found
            elif arr[j] + arr[i] > arr[k]:  # If the sum is greater, decrement `j` to reduce the sum
                j -= 1
            else:  # If the sum is smaller, increment `i` to increase the sum
                i += 1
    
    # If no triplet is found, return False
    return False

"""
Time Complexity:O(n^2)   
Space Complexity: O(1) 

"""




def checkTriplet(arr):
    count_arr = [0] * (max(arr) + 1)  # Create a frequency array to count occurrences of each element in `arr`
    for i in arr:
        count_arr[i] += 1  # Increment the count of the number `i`

    # Iterate over each possible value `i` in the range of the frequency array
    for i in range(len(count_arr)):
        if count_arr[i]:  # Check if `i` exists in the array
            # Iterate over each possible value `j` in the range of the frequency array
            for j in range(len(count_arr)):
                if count_arr[j] and j != i:  # Check if `j` exists and is not equal to `i`
                    c = ((i**2) + (j**2)) ** 0.5  # Calculate the potential hypotenuse (c) as the square root of `i^2 + j^2`
                    
                    # Check if `c` is an integer
                    if int(c) == c:
                        # Explanation for `int(c) == c`:
                        # This ensures that `c` is a whole number. Floating-point operations
                        # might return a value like `5.0` instead of `5`. Using `int(c) == c`
                        # confirms that the calculated value of `c` is a valid integer.
                        
                        # Check if `c` lies within the bounds of the frequency array
                        if c < len(count_arr):
                            # Check if the integer value of `c` exists in the original array
                            if count_arr[int(c)]:
                                return True  # A valid Pythagorean triplet is found

    # If no Pythagorean triplet is found, return False
    return False
"""
Time Complexity:O(max(arr)^2)   
Space Complexity: O(max(arr)) 

"""