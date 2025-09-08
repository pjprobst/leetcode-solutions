// Last updated: 9/8/2025, 4:38:42 PM
class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] answer = new int[]{1,2};
        for (int i=0; i<nums.length; i++){
            for (int j=0; j<nums.length; j++){
                if ((nums[i] + nums[j] == target) && (i != j)){
                    answer[0] = i;
                    answer[1] = j;
                    break;
                }
            }
        }
        return answer;
    }
}