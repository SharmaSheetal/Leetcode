from typing import List
from functools import cmp_to_key
def zigZag(self, n : int, arr : List[int]) -> None:
    position =0 #track even odd position
    for i in range(n-1): #comparing each element with its next neighbor.
        # for even position
        if position==0: 
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
        #for odd position
        if position==1:
            if arr[i]<arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
        position=(position+1)%2
"""
Time complexity:O(n)
Space complexity: O(n)
Auxilary space: O(1)
"""

#Alternate

def zigZag(self, n : int, arr : List[int]) -> None:
        arr.sort()
        # traverse the array from 1 to n-1
        for i in range(1, n-1, 2):
            arr[i], arr[i+1] = arr[i+1], arr[i]
"""
Time complexity:O(nlogn)
Space complexity: O(n)
Auxilary space: O(1)
"""