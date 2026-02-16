# Last updated: 2/15/2026, 8:54:17 PM
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        i = 0
        if n < 0:
            return False
        n = abs(n)
        while n >= math.pow(2, i):
            if (n == math.pow(2, i)):
                return True
            i += 1
        return False