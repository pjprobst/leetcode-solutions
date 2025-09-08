// Last updated: 9/8/2025, 4:38:40 PM
class Solution {
    public String longestCommonPrefix(String[] strs) {
        String answer = "";
        String one ="";
        String two = "";
        boolean cont = true;
        for (int i = 0; i<=200-1; i++){
            for (int j = 0; j<strs.length-1; j++){
                if (strs[j].length() < (i+1)){
                    one = "";
                }
                else {
                    one = ""+strs[j].charAt(i);
                }
                if (strs[j+1].length() < (i+1)){
                    two = "";
                }
                else {
                    two = ""+strs[j+1].charAt(i);
                }
                if (!one.equals(two) || (one.equals("") || two.equals(""))){
                    cont = false;
                }
            }
            if (cont == true){
                answer += one;
            }
            else{
                break;
            }
        }
    if (strs.length == 1 && strs[0].length() == 1){
        return strs[0];
    }
    return answer;
    }
}