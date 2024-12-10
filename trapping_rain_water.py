def trappingWater(self, heights):
    """
    Calculate the total water trapped between the bars using an array-based approach.
    
    Args:
    heights (list): List of integers representing the height of bars.

    Returns:
    int: Total amount of water trapped.
    """
    # Initialize the total water trapped
    total_water = 0

    # Trapping water is only possible if there are more than 2 bars
    if len(heights) > 2:
        n = len(heights)
        
        # Arrays to store the maximum height to the left and right of each index
        left_max = [0] * n
        right_max = [0] * n
        
        # Initialize the first element of left_max and last element of right_max
        left_max[0] = heights[0]
        right_max[-1] = heights[-1]
        
        # Fill the left_max array: Each index contains the maximum height to its left
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], heights[i])
        
        # Fill the right_max array: Each index contains the maximum height to its right
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], heights[i])
        
        # Calculate the water trapped at each index
        for i in range(1, n - 1):  # Skip the first and last bar (no water can be trapped there)
            # Water trapped at index i is the difference between the smaller of the two maxima
            # and the height of the current bar
            total_water += min(left_max[i], right_max[i]) - heights[i]
    
    return total_water
"""
Time Complexity: O(n), 
Space Complexity: O(n). 
"""
