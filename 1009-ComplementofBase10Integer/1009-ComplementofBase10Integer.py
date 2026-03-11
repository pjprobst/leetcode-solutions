# Last updated: 3/11/2026, 7:20:12 PM
1class Solution:
2    def bitwiseComplement(self, n: int) -> int:
3        binary = ""
4        n = bin(n)[2:]
5        for i in n:
6            binary += str(1-int(i))
7        return int(binary, 2)
8