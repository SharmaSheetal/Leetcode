def stockBuySell(arr):
    profit = 0  # Initialize the total profit to 0.
    i = 1  # Start from the second element in the array.
    start = arr[0]  # Set the starting point of the current increasing sequence to the first element.

    # Iterate through the array starting from the second element.
    while i < len(arr):
        # While the current element is greater than or equal to the previous one (indicating an increasing sequence),
        # move to the next element.
        while i < len(arr) and arr[i] >= arr[i - 1]:
            i += 1

        # Add the profit from the current increasing sequence to the total profit.
        # (arr[i-1] is the last element of the increasing sequence)
        profit += (arr[i - 1] - start)

        # If there are more elements left in the array, set `start` to the current element and move `i` to the next element.
        if i < len(arr):
            start = arr[i]
            i += 1

    # If there is any profit, return it; otherwise, return 0.
    if profit:
        return profit
    return 0

def stockBuySell(self, arr):
    n = len(arr)
    profit = 0

    i = 0
    while i < n - 1:
        # Find local minima (buy point)
        while i < n - 1 and arr[i] >= arr[i + 1]:
            i += 1
        lMin = arr[i]

        # Find local maxima (sell point)
        while i < n - 1 and arr[i] <= arr[i + 1]:
            i += 1
        lMax = arr[i]

        # Add profit from the current local minima and maxima
        profit += (lMax - lMin)

    return profit if profit > 0 else 0


"""
Time Complexity: O(n), 
Space Complexity: O(1). 
"""
