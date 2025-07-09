def is_anagram(s, t):
    """
    Check if two strings are anagrams.
    
    Args:
        s: First string
        t: Second string
    
    Returns:
        bool: True if strings are anagrams, False otherwise
    """
    # Early return if lengths are different
    if len(s) != len(t):
        return False
    
    # Method 1: Using dictionary for character counting
    char_count = {}
    
    # Count characters in first string
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Decrement count for second string
    for char in t:
        if char not in char_count:
            return False
        char_count[char] -= 1
        if char_count[char] == 0:
            del char_count[char]
    
    # If dictionary is empty, strings are anagrams
    return len(char_count) == 0

def is_anagram_sorting(s, t):
    """
    Alternative approach using sorting.
    
    Time Complexity: O(n log n)
    Space Complexity: O(1)
    """
    return sorted(s) == sorted(t)

# Main function for HackerRank format
if __name__ == "__main__":
    s = input().strip()
    t = input().strip()
    
    result = is_anagram(s, t)
    print("true" if result else "false")