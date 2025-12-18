

class Solution {
    public boolean isAnagram(String s, String t) {
        // create a 26 int array to hold occurence
        // increment with s, decrement with t
        int[] alphabet = new int[26];
        for (int i = 0; i < s.length(); i++) {
            alphabet[s.charAt(i) - 'a']++;
        }
        for (int j = 0; j < t.length(); j++) {
            alphabet[t.charAt(j) - 'a']--;
        }
        for (int k: alphabet) {
            if (k != 0) {
                return false;
            }
        }
        return true;

    }
}