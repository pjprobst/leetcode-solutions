// Last updated: 9/8/2025, 4:38:32 PM
class Solution {
    public int lengthOfLastWord(String s) {
        int count = 0;
        boolean space = false;
        for (int i = 0; i<s.length(); i++){
            if (s.substring(i, i+1).compareTo(" ") != 0 && space == true){
                count = 1;
                space = false;
            }
            else if (s.substring(i, i+1).compareTo(" ") != 0 && space == false){
                count += 1;
            }
            else {
                space = true;
            }
        }
        return count;
    }
}