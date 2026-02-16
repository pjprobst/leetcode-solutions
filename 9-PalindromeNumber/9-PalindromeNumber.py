# Last updated: 2/15/2026, 8:54:26 PM
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            string = str(x)
            l = 0
            r = len(string)-1
            while(l < r):
                if (string[l] != string[r]):
                    return False
                l += 1
                r -= 1         
            return True