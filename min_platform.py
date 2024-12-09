def minimumPlatform(arr, dep):
    # Sort the arrival and departure lists
    arr.sort()
    dep.sort()

    # Initialize variables:
    count = 0                # Counts the number of platforms currently needed.
    platform_needed = 0      # The maximum number of platforms needed at any given time.
    i, j = 0, 0             # Pointers for iterating through arrival and departure lists.

    # Iterate over the arrival times
    while i < len(arr):
        # If the current train's arrival time is less than or equal to the current train's departure time
        if arr[i] <= dep[j]:
            count += 1   # Increase the count of platforms needed because a new train has arrived.
            i += 1       # Move to the next arrival.
        else:
            count -= 1   # Decrease the count as one train has left (the platform is now free).
            j += 1       # Move to the next departure.
        
        # Update the maximum platforms needed so far
        platform_needed = max(platform_needed, count)

    # Return the result: the maximum platforms needed at any point in time.
    return platform_needed
"""
Time complexity:O(n⋅log(n))
Space complexity: O(1)
"""