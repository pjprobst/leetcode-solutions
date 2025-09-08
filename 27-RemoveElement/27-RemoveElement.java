// Last updated: 9/8/2025, 4:38:37 PM
class Solution {
    public int removeElement(int[] nums, int val) {
        int k = 0;
        for (int i=0; i<nums.length; i++){
            if (nums[i] != val){
                nums[k] = nums[i];
                k++;
            }
        }
    return k;
    }
}