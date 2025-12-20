// Last updated: 12/20/2025, 5:07:32 PM
1class Solution {
2    public int minDeletionSize(String[] strs) {
3        boolean sorted = true;
4        int count = 0;
5        for (int i = 0; i<strs[0].length(); i++){
6            for (int j = 1; j<strs.length; j++){
7                if (strs[j-1].charAt(i) > strs[j].charAt(i)){
8                    count++;
9                    break;
10                }
11            }
12        }
13        return count;
14    }
15}