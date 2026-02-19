# Last updated: 2/18/2026, 10:02:54 PM
1class Solution:
2    def addDigits(self, num: int) -> int:
3        num = str(num)
4        total = 0
5        for l in num:
6            total += int(l)
7        
8        if total < 10:
9            return total
10        res = None
11        while res is None:
12            res = self.addDigits(total)
13        return res