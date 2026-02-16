// Last updated: 2/15/2026, 8:54:18 PM
class Solution {
    public int mySqrt(int x) {
        int difference = 1;
        int sqrt;
        int i = 0;
        while(difference >= 0){
            sqrt = (i * i);
            difference = (x-sqrt);
            i++;
        }
        return i-2;
    }
}