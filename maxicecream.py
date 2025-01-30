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
