"""

It is a sweltering summer day, and a boy wants to buy some ice cream bars.
At the store, there are n ice cream bars. You are given an array costs of length n, where costs[i] is the price of the ith ice cream bar in coins. The boy initially has coins coins to spend, and he wants to buy as many ice cream bars as possible. 
Note: The boy can buy the ice cream bars in any order.
Return the maximum number of ice cream bars the boy can buy with coins coins.
You must solve the problem by counting sort.
Example 1:
Input: costs = [1,3,2,4,1], coins = 7
Output: 4
Explanation: The boy can buy ice cream bars at indices 0,1,2,4 for a total price of 1 + 3 + 2 + 1 = 7.
"""
from typing import List

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        # Sort the costs in ascending order to prioritize cheaper ice creams
        costs.sort()
        
        bars_purchased = 0  # Counter for the number of ice cream bars bought
        index = 0  # Pointer to iterate through the sorted list
        
        # Iterate while there are ice creams left and we have enough coins
        while index < len(costs) and coins >= costs[index]:
            coins -= costs[index]  # Deduct the cost of the current ice cream bar
            bars_purchased += 1  # Increase the count of ice creams bought
            index += 1  # Move to the next ice cream price
        
        return bars_purchased  # Return the total number of ice creams bought
"""
Time Complexity:O(nlogn)   
Space Complexity: O(1) 

"""