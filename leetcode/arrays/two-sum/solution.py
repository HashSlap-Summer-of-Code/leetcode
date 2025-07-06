def twoSum(nums, target):
    """
    Find two numbers in array that add up to target.
    
    Args:
        nums: List of integers
        target: Target sum
    
    Returns:
        List of two indices
    """
    num_map = {}  # value -> index
    
    for i, num in enumerate(nums):
        complement = target - num
        
        # Check if complement exists in map
        if complement in num_map:
            return [num_map[complement], i]
        
        # Add current number and its index to map
        num_map[num] = i
    
    return []  # Should never reach here given problem constraints

# Example usage:
# nums = [2, 7, 11, 15]
# target = 9
# result = twoSum(nums, target)  # Returns [0, 1]