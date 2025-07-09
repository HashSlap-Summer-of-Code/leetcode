import java.util.*;

public class solution {
    
    public static boolean isAnagram(String s, String t) {
        // Early return if lengths are different
        if (s.length() != t.length()) {
            return false;
        }
        
        // Frequency array for 26 lowercase letters
        int[] charCount = new int[26];
        
        // Count characters in both strings
        for (int i = 0; i < s.length(); i++) {
            charCount[s.charAt(i) - 'a']++;    // Increment for first string
            charCount[t.charAt(i) - 'a']--;    // Decrement for second string
        }
        
        // Check if all counts are zero (balanced)
        for (int count : charCount) {
            if (count != 0) {
                return false;
            }
        }
        
        return true;
    }
    
    // Alternative approach using HashMap
    public static boolean isAnagramHashMap(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        
        Map<Character, Integer> charCount = new HashMap<>();
        
        // Count characters in first string
        for (char c : s.toCharArray()) {
            charCount.put(c, charCount.getOrDefault(c, 0) + 1);
        }
        
        // Decrement count for second string
        for (char c : t.toCharArray()) {
            if (!charCount.containsKey(c)) {
                return false;
            }
            charCount.put(c, charCount.get(c) - 1);
            if (charCount.get(c) == 0) {
                charCount.remove(c);
            }
        }
        
        return charCount.isEmpty();
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String s = scanner.nextLine().trim();
        String t = scanner.nextLine().trim();
        
        boolean result = isAnagram(s, t);
        System.out.println(result ? "true" : "false");
        
        scanner.close();
    }
}