// Last updated: 9/8/2025, 4:38:33 PM
import java.util.Random;
class Solution {
    public String findDifferentBinaryString(String[] nums) {
        Random rand = new Random();
        HashMap<String, Integer> hash_map = new HashMap<String, Integer>();
        String ubinary = "";
        for(int i = 0; i<nums.length; i++){
            hash_map.put(nums[i], i);
        }
        while(hash_map.containsKey(ubinary) || ubinary == ""){
            ubinary = "";
            for(int j = 0; j<nums.length; j++){
                 ubinary += ""+rand.nextInt(2);
        
            }
            System.out.println(ubinary);
        }
        return ubinary;
    }
}