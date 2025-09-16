// Last updated: 9/16/2025, 6:53:49 PM
class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        int max = 0;
        List<Boolean> booleanList = new ArrayList<>();
        for (int i = 0; i < candies.length; i++){
            if (candies[i]>max){
                max = candies[i];
            }
        }
        for (int j = 0; j < candies.length; j++){
            if (candies[j] + extraCandies >= max){
                booleanList.add(true);
            }
            else {
                booleanList.add(false);
            }
        }
        return booleanList;
    }
}