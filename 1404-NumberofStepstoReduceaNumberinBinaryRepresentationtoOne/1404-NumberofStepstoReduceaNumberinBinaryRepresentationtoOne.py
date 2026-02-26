# Last updated: 2/25/2026, 7:14:01 PM
1class Solution:
2    def numSteps(self, s: str) -> int:
3        count = 0
4        num = self.binaryToInt(s)
5        print(num)
6        while num != 1:
7            if num % 2 == 0:
8                num = num // 2
9            else:
10                num += 1
11            count += 1
12        return count
13    def binaryToInt(self, s: str) -> int:
14        total = 0
15        add = int(math.pow(2, len(s)-1))
16        for l in s:
17            if l == "1":
18                total += int(add)
19            add = int(add // 2)
20        return total