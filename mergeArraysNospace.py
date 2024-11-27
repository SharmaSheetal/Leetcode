def mergeArrays(self, a, b):
    i=len(a)-1 #pointing at the larger element at a
    j=0 #point at the smallest emelent at b
    while i>=0 and j<len(b):
        if a[i]>=b[j]:
            a[i],b[j]=b[j],a[i]
        i-=1 
        j+=1
    a.sort()
    b.sort()
"""
Time complexity:O(n⋅log(n))+O(m⋅log(m))
Space complexity: O(1)
"""


def mergeArrays(a, b):
    n = len(a)  # Length of the first array
    m = len(b)  # Length of the second array
    gap = (n + m + 1) // 2  # Initial gap size, calculated as ceiling of (n + m) / 2

    # Continue until the gap reduces to 0
    while gap > 0:
        i = 0  # Pointer for the first element
        j = gap  # Pointer for the element at the "gap" distance

        # Traverse both arrays using the pointers `i` and `j`
        while j < n + m:
            # Case 1: Both pointers are in the first array `a`
            if j < n and a[i] > a[j]:
                # Swap elements if they are out of order
                a[i], a[j] = a[j], a[i]

            # Case 2: Pointer `i` is in `a` and pointer `j` is in `b`
            elif i < n and j >= n and a[i] > b[j - n]:
                # Swap elements if `a[i]` is larger than the corresponding element in `b`
                a[i], b[j - n] = b[j - n], a[i]

            # Case 3: Both pointers are in the second array `b`
            elif i >= n and j >= n and b[i - n] > b[j - n]:
                # Swap elements if they are out of order in `b`
                b[i - n], b[j - n] = b[j - n], b[i - n]

            # Move both pointers forward
            i += 1
            j += 1

        # If the gap becomes 1, break the loop after this iteration
        if gap == 1:
            break

        # Calculate the next gap using the Shell Sort method
        gap = (gap + 1) // 2

"""
Time complexity:O(m+n)⋅log(m+n)
Space complexity: O(1)
"""