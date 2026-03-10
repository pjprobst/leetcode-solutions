# Last updated: 3/10/2026, 5:51:50 PM
class Solution:
    def concatenatedBinary(self, n: int) -> int:
        total = ""
        for i in range(1, n+1):
            total += bin(i)[2:]
        
        return int(total, 2) % (10**9 + 7)