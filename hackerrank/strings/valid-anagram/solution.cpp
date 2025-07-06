#include <iostream>
#include <string>
#include <vector>
using namespace std;

bool isAnagram(string s, string t) {
    // Early return if lengths are different
    if (s.length() != t.length()) {
        return false;
    }
    
    // Frequency array for 26 lowercase letters
    vector<int> charCount(26, 0);
    
    // Count characters in both strings
    for (int i = 0; i < s.length(); i++) {
        charCount[s[i] - 'a']++;    // Increment for first string
        charCount[t[i] - 'a']--;    // Decrement for second string
    }
    
    // Check if all counts are zero (balanced)
    for (int count : charCount) {
        if (count != 0) {
            return false;
        }
    }
    
    return true;
}

int main() {
    string s, t;
    cin >> s >> t;
    
    bool result = isAnagram(s, t);
    cout << (result ? "true" : "false") << endl;
    
    return 0;
}