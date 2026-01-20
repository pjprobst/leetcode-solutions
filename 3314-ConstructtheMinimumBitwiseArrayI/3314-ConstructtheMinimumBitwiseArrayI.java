// Last updated: 1/19/2026, 10:49:08 PM
1class Solution {
2    public int[] minBitwiseArray(List<Integer> nums) {
3        String[] binary = new String[nums.size()];
4        int[] sol = new int[nums.size()];
5
6        for (int i = 0; i < nums.size(); i++){
7            for (int j = 0; j <= 999; j++){
8                if ((j | (j+1)) == nums.get(i)){
9                    sol[i] = j;
10                    break;
11                }
12            }
13            if (sol[i] == 0){
14                sol[i] = -1;
15            }
16        }
17        return sol;     
18    }
19}