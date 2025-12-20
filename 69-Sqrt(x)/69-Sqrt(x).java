// Last updated: 12/20/2025, 5:56:44 PM
1class Solution {
2    public int mySqrt(int x) {
3        int difference = 1;
4        int sqrt;
5        int i = 0;
6        while(difference >= 0){
7            sqrt = (i * i);
8            difference = (x-sqrt);
9            i++;
10        }
11        return i-2;
12    }
13}