# Last updated: 2/28/2026, 2:04:02 AM
1class Solution:
2    def concatenatedBinary(self, n: int) -> int:
3        total = ""
4        for i in range(1, n+1):
5            total += bin(i)[2:]
6        
7        return int(total, 2) % (10**9 + 7)