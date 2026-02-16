# Last updated: 2/15/2026, 8:54:09 PM
class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        count = 0
        for i in range(1, min(a,b) + 1):
            if a % i == 0 and b % i == 0:
                count += 1
        return count
        