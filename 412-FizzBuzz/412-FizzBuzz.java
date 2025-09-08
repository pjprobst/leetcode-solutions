// Last updated: 9/8/2025, 4:38:36 PM
class Solution {
    public List<String> fizzBuzz(int n) {
        List<String> answer = new ArrayList<String>();
        for (int i=1; i<n+1; i++){
            if (((i % 3) == 0) && ((i % 5) != 0)){
                answer.add("Fizz");
            }
            else if (((i % 5) == 0) && ((i % 3) != 0)){
                answer.add("Buzz");
            }
            else if (((i % 5) == 0) && ((i % 3) == 0)){
                answer.add("FizzBuzz");
            }
            else{
                answer.add(String.valueOf(i));
            }
        }
        return answer;
    }
}