# Last updated: 2/19/2026, 9:48:31 AM
1class Solution:
2    def processStr(self, s: str) -> str:
3        res = ""
4        for l in s:
5            if l == '*':
6                if len(res) - 1 in range(len(res)):
7                    res = res[0:len(res)-1]
8            elif l == '#':
9                res = res + res
10            elif l == '%':
11                res = res[::-1]
12            else:
13                res = res + str(l)
14        return res