""" 
Longest Substring Without Repeating Characters
O(N)

"""

"""
Algorithm used: Kadanes algo

"""
def lengthOfLongestSubstring(self, s):
    """
    :type s: str
    :rtype: int
    """
    if len(set(s)) == len(s):  #if str has all unique char
            return len(s)
    substring = ''
    maxLen = 0
    for i in s:
        if i not in substring: #if char not encountered then add the i in substring and return max of len(substring) and maxlen
            substring = substring + i
            maxLen = max(maxLen, len(substring))
        else: #find the position of the repeating char and start the new substring from position +1 and add the repeating char at the end
            j=substring.index(i)
            substring=substring[j+1:]+i
    return maxLen