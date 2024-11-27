def subArraySum(arr, target):
        # code here
        def find_subarray(arr):
            s=0
            j,i=0,0
            while i<=j and j<len(arr):
                s+=arr[j]
                # Multiple elements need to be removed to bring s back to the target range.
                while s>target:
                    s-=arr[i]
                    i+=1
                if s==target:
                    return [i+1,j+1]
                j+=1
            
            return [-1]
        if target in arr:
            t=arr.index(target)
            temp_result=find_subarray(arr[:t])
            if -1 in temp_result:
                return [t+1,t+1]
            else:
                return temp_result
        else:
            return find_subarray(arr)
"""
Time complexity: O(n)
Auxilary Space : O(1)
"""