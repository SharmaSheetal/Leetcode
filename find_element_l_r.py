def findElement(arr):
        l_max,r_min=[0]*(len(arr)),[max(arr)+1]*(len(arr))
        l_max[0],r_min[-1]=arr[0],arr[-1]
    
        #Traverse input array from left to right and fill l_max[] such that l_max[i] contains a maximum element from 0 to i in the input array.
        for i in range(1,len(arr)): 
            l_max[i]=max(arr[i],l_max[i-1])
        #Traverse input array from right to left and fill r_min[] such that r_min[i] contains a minimum element from to n-1 to i in the input array.
        for i in range(len(arr)-2,-1,-1):
            r_min[i]=min(arr[i],r_min[i+1])
        for i in range(1,len(arr)-1):
            if l_max[i-1]<=arr[i] and r_min[i+1]>=arr[i]:
                return arr[i]
        return -1
"""
Time complexity: O(n)
Auxilary space: O(n)
"""
def findElement(arr):
        for i in range(1,len(arr)-1):
            if arr[i] > max(arr[i-1::-1]) and arr[i] < min(arr[i+1:]):
                return arr[i]
        return -1
"""
Time complexity: O(n^2)
Auxilary space: O(n)
"""