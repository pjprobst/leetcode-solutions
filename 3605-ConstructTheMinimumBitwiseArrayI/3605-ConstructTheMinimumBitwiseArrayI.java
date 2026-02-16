// Last updated: 2/15/2026, 8:54:07 PM
class Solution {
    public int[] minBitwiseArray(List<Integer> nums) {
        String[] binary = new String[nums.size()];
        int[] sol = new int[nums.size()];

        for (int i = 0; i < nums.size(); i++){
            for (int j = 0; j <= 999; j++){
                if ((j | (j+1)) == nums.get(i)){
                    sol[i] = j;
                    break;
                }
            }
            if (sol[i] == 0){
                sol[i] = -1;
            }
        }
        return sol;     
    }
}