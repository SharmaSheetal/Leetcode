from functools import cmp_to_key
def printLargest(arr):
    result = ""
    def compare(a,b):
        #The comparison (a + b > b + a) evaluates correctly because strings in Python are compared lexicographically.
        if a+b>b+a:
            return -1
        return 1
    """
    Return -1:
	• Indicates that the first element (a) should come before the second element (b).
    Return 1:
	• Indicates that the first element (a) should come after the second element (b).
    Return 0:
    • Indicates that a and b are equal, and their order does not matter.
    """
    arr=sorted(arr,key=cmp_to_key(compare))
    result="".join(arr)
    # Handle the case where all numbers are zero
    if result[0] == '0':
        return '0'

    return result

"""
Time Complexity:  O(n log n)
Auxiliary Space: O(1)
Space Complexity: O(𝑛⋅𝑘) wherr n is the len of array and average length of each string is k
"""
