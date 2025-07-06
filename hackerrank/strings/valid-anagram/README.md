# Valid Anagram – HackerRank

## 🧩 Problem Statement

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

**Constraints:**
- 1 ≤ s.length, t.length ≤ 5 * 10⁴
- s and t consist of lowercase English letters only

**Examples:**
- Input: s = "anagram", t = "nagaram" → Output: true
- Input: s = "rat", t = "car" → Output: false

## 💡 Approach

**Frequency Count Approach:**
- Count the frequency of each character in both strings
- Compare the frequency maps - if identical, strings are anagrams
- Early return false if lengths are different

**Alternative Approach:**
- Sort both strings and compare if they're equal

**Time Complexity:** O(n) - Single pass through both strings
**Space Complexity:** O(1) - Fixed size array for 26 lowercase letters

## 📜 Code Explanation

1. **Length Check:** If strings have different lengths, they cannot be anagrams
2. **Frequency Counting:** Use an array/map to count character frequencies
3. **Increment/Decrement:** Increment count for first string, decrement for second
4. **Validation:** Check if all counts are zero (balanced)

## 🔗 Problem Link

[View on HackerRank](https://www.hackerrank.com/challenges/anagram/problem)