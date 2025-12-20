// Last updated: 12/20/2025, 5:07:42 PM
1class Solution {
2    public int minDeletionSize(String[] strs) {
3        int count = 0;
4        for (int i = 0; i<strs[0].length(); i++){
5            for (int j = 1; j<strs.length; j++){
6                if (strs[j-1].charAt(i) > strs[j].charAt(i)){
7                    count++;
8                    break;
9                }
10            }
11        }
12        return count;
13    }
14}