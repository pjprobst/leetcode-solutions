// Last updated: 9/8/2025, 4:38:38 PM
class Solution {
    public int removeDuplicates(int[] nums) {
        int prevnum = 101;
        int k = 0;
        for (int i = 0; i < nums.length; i++){
            if (nums[i] != prevnum){
                nums[k] = nums[i];
                k+=1;
                prevnum = nums[i];
            }
        }
        return k;
    }
}