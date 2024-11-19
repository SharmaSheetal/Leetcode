def lastIndex(self, s: str) -> int:
        for i in range(len(s)-1,-1,-1):
            if s[i]=='1':
                return i
        return -1
"""
Time Complexity: O(n)
Auxillary Space: O(1)
Space Complexity: O(n)
"""