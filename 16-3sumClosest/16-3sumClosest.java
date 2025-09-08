// Last updated: 9/8/2025, 4:38:39 PM
import java.lang.Math;
class Solution {
    public int threeSumClosest(int[] nums, int target) {
        int dif = 1000000;
        int answer = 0;
        for (int i =0; i<nums.length-2; i++){
            for (int j =i+1; j<nums.length-1; j++){
                for (int k=j+1; k<nums.length; k++){
                    if (Math.abs((nums[i] + nums[j] + nums[k]) - target) < dif){
                        answer = (nums[i] + nums[j] + nums[k]);
                        dif = (Math.abs((nums[i] + nums[j] + nums[k]) - target));
                    }
                }
            }
        }
    return answer;
    }
}