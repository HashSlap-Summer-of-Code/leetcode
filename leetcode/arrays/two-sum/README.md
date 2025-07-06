# Two Sum – LeetCode

## 🧩 Problem Statement

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to target.

**Constraints:**
- 2 ≤ nums.length ≤ 10⁴
- -10⁹ ≤ nums[i] ≤ 10⁹
- -10⁹ ≤ target ≤ 10⁹
- Only one valid answer exists.

## 💡 Approach

**Hash Map Approach:**
- Use a hash map to store each number and its index as we iterate
- For each element, check if `target - current_element` exists in the hash map
- If found, return the indices; otherwise, add current element to hash map

**Time Complexity:** O(n) - Single pass through array
**Space Complexity:** O(n) - Hash map storage

## 📜 Code Explanation

1. **Initialize** an empty hash map to store number-index pairs
2. **Iterate** through the array with both value and index
3. **Calculate** the complement needed: `complement = target - current_number`
4. **Check** if complement exists in hash map
5. **Return** indices if found, otherwise add current number to hash map

## 🔗 Problem Link

[View on LeetCode](https://leetcode.com/problems/two-sum/)