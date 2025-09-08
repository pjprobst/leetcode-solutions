// Last updated: 9/8/2025, 4:38:36 PM
class Solution {
    public int strStr(String haystack, String needle) {
        int index = -1;
        for (int i = 0; i<=(haystack.length() - needle.length()); i++){
            if (haystack.substring(i, needle.length()+i).compareTo(needle) == 0){
                index = i;
                break;
            }
        }
        return index;   
    }
}