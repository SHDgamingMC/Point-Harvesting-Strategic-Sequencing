def max_points(sequence):
    points = {}  # Dictionary to store maximum points at each index
    
    # Initialize base cases
    points[-1] = 0
    points[0] = 0 if sequence[0] == 0 else sequence[0]
    
    for i in range(1, len(sequence)):
        if sequence[i] == sequence[i - 1]:
            # If the current number is the same as the previous one,
            # there's no point in picking the current number, so we
            # just carry forward the maximum points from the previous index
            points[i] = points[i - 1]
        else:
            # Otherwise, we either pick the current number and skip
            # the adjacent numbers, or skip the current number and
            # carry forward the maximum points from the previous index
            points[i] = max(points[i - 1], points[i - 2] + sequence[i])
    
    return points[len(sequence) - 1]

# Example usage:
sequence = [3, 4, 2, 2, 3, 5, 1]
print("Maximum points:", max_points(sequence))

# BY SUVIN