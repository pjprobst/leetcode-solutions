# Last updated: 3/4/2026, 8:15:21 PM
1class Solution:
2    def minOperations(self, s: str) -> int:
3        if len(s) % 2 == 0:
4            poss1 = "01" * (len(s)//2)
5            poss2 = "10" * (len(s)//2)
6        else:
7            poss1 = ("01" * (len(s)//2)) + "0"
8            poss2 = ("10" * (len(s)//2)) + "1"
9
10        count1 = sum(1 for a, b in zip(s, poss1) if a != b)
11        count2 = sum(1 for a, b in zip(s, poss2) if a != b)
12
13        return min(count1, len(s) - count1)