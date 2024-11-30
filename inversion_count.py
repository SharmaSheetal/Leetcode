def inversionCount(arr):
    # Initialize the inversion count
    c = 0

    # Outer loop: Iterate from the end of the array to the second element
    i = len(arr) - 1
    while i > 0:
        # Inner loop: Compare the current element with all previous elements
        j = i - 1
        while j >= 0:
            # Check if an inversion exists (arr[i] < arr[j])
            if arr[i] < arr[j]:
                c += 1  # Increment the count for each inversion found
            j -= 1  # Move to the previous element in the array
        i -= 1  # Move the outer loop pointer to the previous element

    # Return the total count of inversions
    return c
"""
Time Complexity:  O(n^2)
Auxiliary Space: O(1)
"""

def inversionCount(arr):
    def merge(array, start, mid, end):
        # Initialize the inversion count and pointers
        inversion_count = 0
        left_index, right_index, sorted_index = 0, 0, start

        # Create left and right subarrays
        left_subarray = array[start:mid + 1]  # Left subarray: from index `start` to `mid`
        right_subarray = array[mid + 1:end + 1]  # Right subarray: from `mid+1` to `end`

        # Merge the two subarrays while counting inversions
        while left_index < len(left_subarray) and right_index < len(right_subarray):
            if left_subarray[left_index] <= right_subarray[right_index]:
                # No inversion, place left_subarray[left_index] in sorted order
                array[sorted_index] = left_subarray[left_index]
                left_index += 1
            else:
                # Inversion found: all remaining elements in `left_subarray[left_index:]` are > right_subarray[right_index]
                inversion_count += len(left_subarray) - left_index
                array[sorted_index] = right_subarray[right_index]
                right_index += 1
            sorted_index += 1

        # Copy any remaining elements from the left subarray
        while left_index < len(left_subarray):
            array[sorted_index] = left_subarray[left_index]
            left_index += 1
            sorted_index += 1

        # Copy any remaining elements from the right subarray
        while right_index < len(right_subarray):
            array[sorted_index] = right_subarray[right_index]
            right_index += 1
            sorted_index += 1

        return inversion_count  # Return the count of inversions found during this merge step


    def count_inversions_using_mergesort(array, start, end):
        # Initialize inversion count
        inversion_count = 0

        # Proceed only if there are at least two elements to sort/merge
        if start < end:
            mid = (start + end) // 2  # Find the midpoint

            # Count inversions in the left subarray
            inversion_count += count_inversions_using_mergesort(array, start, mid)

            # Count inversions in the right subarray
            inversion_count += count_inversions_using_mergesort(array, mid + 1, end)

            # Count inversions between the left and right subarrays during merge
            inversion_count += merge(array, start, mid, end)

        return inversion_count  
    return count_inversions_using_mergesort(arr,0,len(arr)-1)
        
"""
Time Complexity:  O(n log n)
Auxiliary Space: O(n)
"""