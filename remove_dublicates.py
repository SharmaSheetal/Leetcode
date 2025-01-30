"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
"""
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Initialize two pointers: `k` will track the position of unique elements,
        # and `i` will iterate through the list.
        k, i = 1, 1
        
        # Traverse through the list starting from index 1.
        while i < len(nums):
            # If the current element (nums[i]) is not equal to the previous element (nums[i-1]),
            # it means we found a unique element.
            if nums[i - 1] != nums[i]:
                # Place the unique element at the position `k`
                nums[k] = nums[i]
                # Increment `k` to track the next position for a unique element.
                k += 1
            # Move the pointer `i` forward to continue checking the next element.
            i += 1
        
        # Return `k`, which represents the number of unique elements in the modified list.
        return k
"""
Time Complexity: O(n)
Space Complexity: O(1)
"""
# Alternatively, you can use the `set` data structure to remove duplicates from the list.
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Convert `nums` to a set to remove duplicates, then back to a list.
        # This ensures all duplicates are removed, but sets do not maintain order.
        nums_ = list(set(nums))
        
        # Sort the list to restore order (if necessary). This step makes sure the unique
        # elements are ordered in non-decreasing order.
        nums_.sort()

        # Assign the unique elements back to the original `nums` list.
        # This overwrites the first `len(nums_)` elements of `nums` with the unique elements.
        for i in range(len(nums_)):
            nums[i] = nums_[i]

        # Return the number of unique elements, which is the length of `nums_`.
        return len(nums_)
"""
Time Complexity: O(nlogn)
Space Complexity: O(n)
"""