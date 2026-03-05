# Last updated: 3/4/2026, 8:15:49 PM
1class Solution:
2    def minOperations(self, s: str) -> int:
3        if len(s) % 2 == 0:
4            poss = "01" * (len(s)//2)
5        else:
6            poss = ("01" * (len(s)//2)) + "0"
7
8        count = sum(1 for a, b in zip(s, poss) if a != b)
9
10        return min(count, len(s) - count)