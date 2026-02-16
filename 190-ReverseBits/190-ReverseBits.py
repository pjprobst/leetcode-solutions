# Last updated: 2/16/2026, 11:58:47 AM
1class Solution:
2    def reverseBits(self, n: int) -> int:
3        return int(format(n, '032b')[::-1], 2)