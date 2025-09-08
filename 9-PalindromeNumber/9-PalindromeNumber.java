// Last updated: 9/8/2025, 4:38:42 PM
class Solution {
    public boolean isPalindrome(int x) {
        String y = ""+x;
        String reverse ="";
        for(int i = y.length()-1; i>=0; i--){
            reverse+=y.charAt(i);
        }
        return reverse.equals(y);
    }
}