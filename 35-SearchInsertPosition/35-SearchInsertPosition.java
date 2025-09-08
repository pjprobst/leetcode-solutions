// Last updated: 9/8/2025, 4:38:35 PM
class Solution {
    public int searchInsert(int[] nums, int target) {
        int answer =0;
        for (int i=0; i<nums.length; i++){
            if (i < nums.length-1){
                if (nums[i] == target){
                    answer = i;
                    break;
                }
                else if (nums[i] < target && nums[i+1] > target){
                    answer = i+1;
                    break;
                }
            }
            else{
                if (target > nums[nums.length-1]){
                    answer = i+1;
                    break;
                }
                else if (target == nums[nums.length-1]){
                    answer = i;
                    break;
                }
                else {
                    answer = 0;
                    break;
                }
            }
        }
        return answer;
    }
}