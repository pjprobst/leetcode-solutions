// Last updated: 9/8/2025, 4:38:39 PM
class Solution {
    public boolean isValid(String s) {
        for (int i = 1; i < s.length(); i++){
            if (s.substring(i-1, i+1).compareTo("()") == 0 || s.substring(i-1, i+1).compareTo("{}") == 0 || s.substring(i-1, i+1).compareTo("[]") == 0){
                return isValid(s.substring(0, i-1) + s.substring(i+1, s.length()));
            }
        }
        if (s.length() != 0){
            return false;
        }
        else {
            return true;
        }
    }
}