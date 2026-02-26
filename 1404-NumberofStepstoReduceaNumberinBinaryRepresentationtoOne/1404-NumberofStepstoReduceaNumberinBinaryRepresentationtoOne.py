# Last updated: 2/25/2026, 7:14:11 PM
1class Solution:
2    def numSteps(self, s: str) -> int:
3        count = 0
4        num = self.binaryToInt(s)
5        while num != 1:
6            if num % 2 == 0:
7                num = num // 2
8            else:
9                num += 1
10            count += 1
11        return count
12    def binaryToInt(self, s: str) -> int:
13        total = 0
14        add = int(math.pow(2, len(s)-1))
15        for l in s:
16            if l == "1":
17                total += int(add)
18            add = int(add // 2)
19        return total