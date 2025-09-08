// Last updated: 9/8/2025, 4:38:34 PM
class Solution {
    public int[] plusOne(int[] digits) {
        for (int i = digits.length-1; i >= 0; i--){
            if ((digits[i]) >= 9){
                if (i < 1){
                    digits[i] = 0;
                    int[] ndigits = new int[digits.length+1];
                    ndigits[0] = 1;
                    for (int j = 1; j < ndigits.length; j++){
                        ndigits[j] = digits[j-1];
                    }
                    return ndigits;
                }
                else{
                    digits[i] = 0;
                    digits[i-1] += 1;
                    if (digits[i-1] <= 9){
                        break;
                    }
                }
            }
            else {
                digits[i] += 1;
                break;
            }
        }
        return digits;
}
}