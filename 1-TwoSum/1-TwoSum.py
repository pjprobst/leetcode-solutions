# Last updated: 2/12/2026, 3:29:25 PM
1class Solution:
2    def isPalindrome(self, x: int) -> bool:
3        if x < 0:
4            return False
5        else:
6            string = str(x)
7            l = 0
8            r = len(string)-1
9            while(l < r):
10                if (string[l] != string[r]):
11                    return False
12                l += 1
13                r -= 1         
14            return True