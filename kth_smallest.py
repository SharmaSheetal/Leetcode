import heapq

def kthSmallest(arr,k):
    maxHeap=[]
    for i in arr:
        heapq.heappush(maxHeap,-i)
        if len(maxHeap)>k:
            heapq.heappop(maxHeap)
    return -heapq.heappop(maxHeap)


"""
Time Complexity: O(nlogk)
Space Complexity: O(k)

"""

def kthSmallest(self, arr,k):
    arr.sort()
    return arr[k-1]

"""
Time Complexity: O(nlogn)
Space Complexity: O(1)

"""

def kthSmallest(self, arr, k):
    # Partition function for the Quickselect algorithm
    def partition(A, l, u):
        start, end = l, u  # Initialize pointers for the start and end of the subarray
        pivot = A[l]  # Choose the first element as the pivot

        # Rearrange the array by placing elements smaller than the pivot on the left
        # and larger elements on the right
        while start < end:
            # Increment the start pointer while the element at start is less than or equal to the pivot
            while A[start] <= pivot and start < u:
                start += 1

            # Decrement the end pointer while the element at end is greater than the pivot
            while A[end] > pivot and end > l:
                end -= 1

            # Swap elements at start and end if they are not yet in the correct position
            if start < end:
                A[start], A[end] = A[end], A[start]

        # Swap the pivot with the element at the end position to place the pivot in its correct sorted position
        A[end], A[l] = A[l], A[end]

        # Return the index of the pivot's final position
        return end

    # Quickselect function to find the kth smallest element
    def quick_select(arr, l, u):
        if l <= u:  # Base case: continue if the subarray has more than one element
            loc = partition(arr, l, u)  # Partition the array and get the pivot's position

            # If the pivot's position matches the k-1 (0-based index), return it as the kth smallest element
            if loc == k - 1:
                return arr[loc]
            # If the pivot's position is greater than k-1, search in the left subarray
            elif loc > k - 1:
                return quick_select(arr, l, loc - 1)
            # If the pivot's position is less than k-1, search in the right subarray
            else:
                return quick_select(arr, loc + 1, u)
        
        # Return None if the bounds are invalid (base case for recursion)
        return None

    # Start the Quickselect process with the entire array
    return quick_select(arr, 0, len(arr) - 1)
"""
Time Complexity : O(n^2) in the worst case, but on average works in O(n Log n) time and performs better than priority queue based algorithm.
Auxiliary Space : O(n) for recursion call stack in worst case. On average : O(Log n)
"""

def kthSmallest(arr, k):
        # Create a frequency array where the index represents the value
        max_value = max(arr)
        frequency = [0] * (max_value + 1)
        
        # Populate the frequency array
        for num in arr:
            frequency[num] += 1
    
        # Accumulate the frequency to find the position of elements
        accumulated_count = 0
        for value in range(len(frequency)):
            if frequency[value] > 0:
                accumulated_count += frequency[value]
                # Check if the accumulated count has reached k
                if accumulated_count >= k:
                    return value  # Return the current value as the kth smallest element
    
        # If we don't find the kth smallest element, return None
        return None

"""
Time Complexity: O(N + max_element), where max_element is the maximum element of the array.
Auxiliary Space: O(max_element)
"""