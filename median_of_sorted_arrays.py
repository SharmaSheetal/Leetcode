"""
Problem Statement:

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).
 
Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

"""

"""
Use case1
[3]
[-2,-1]
even though  len a < lenb max(b)< min(b)

Use case 2:
Where all left subarray is from only one array


use case 3:
Empty array

"""
"""
Algorithm Used : Binary Search 

"""
def findMedianSortedArrays_binary_search(nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        A, B = nums1, nums2
        #case where either one of them is empty
        if len(A) == 0:
            if len(B)==0:
                return -1
            else:
                if len(B) % 2 == 0:
                    return (B[len(B) // 2] + B[(len(B) // 2) - 1]) / 2.0
                else:
                    return B[len(B) // 2]
        total = len(A) + len(B)
        #If nums1 is larger than nums2, they are swapped to ensure A is the smaller array. This optimizes the binary search range.
        if len(nums1) > len(nums2):
            A, B = B, A
        half = total // 2
        l, r = 0, len(A) - 1
        #Binary Search Setup:
        while True:
            mid_a = (l + r) // 2  # pointer in a
            mid_all = half - mid_a - 2
            #If mid_a is out of bounds on the left side (meaning the partition lies entirely in B), it assigns the left boundary from B and the right boundary from the first element of A.
            if mid_a<0:
                Aleft = B[mid_all]
                #Aright is set to A[0], as Aright must take the smallest possible element from A if it’s available.
                Aright=A[0]
            else:
                Aleft = A[mid_a]
                Aright = A[mid_a + 1] if mid_a + 1 < len(A) else float('infinity')
            if mid_all>=0:
                Bleft = B[mid_all]
                Bright = B[mid_all + 1] if mid_all + 1 < len(B) else float('infinity')
            #This situation occurs if the partition lies entirely in A and mid_all is -1 or smaller.
            else:
                #In this case, Bleft would take the value of Aleft, and Bright would take the first element of B, making B[0] the smallest right-bound element in B.
                Bleft=Aleft
                Bright=B[0]
                # correct partition
            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if total % 2:
                    return min(Bright, Aright)
                else:
                    return (max(Bleft, Aleft) + min(Aright, Bright)) / 2.0
            elif Aleft > Bright:
                r = mid_a - 1
            else:
                l = mid_a + 1 

def findMedianSortedArrays(self, nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    if nums1 is None:
        nums1=[]
    if nums2 is None:
        nums2=[]   
    sort=sorted(nums1+nums2) 
    l=len(sort)
    if l%2!=0:
        return float(sort[l//2])
    else:
        mid1=l//2-1
        mid2=l//2
        return (sort[mid1]+sort[mid2])/2.0
