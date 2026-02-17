# Last updated: 2/16/2026, 9:09:31 PM
1class Solution:
2    def isValid(self, s: str) -> bool:
3        pairs = {"()", "[]", "{}"}
4        res = s
5        i = 0
6        while res != "":
7            if i > len(res) - 1:
8                break
9            if res[i:i+2] in pairs:
10                if i is 0:
11                    res = res[i+2:len(res)]
12                elif i is len(res)-2:
13                    res = res[0:i]
14                else:
15                    res = res[0:i] + res[i+2:len(res)]
16                i = 0
17            else:
18                i += 1
19        if res == "":
20            return True
21        return False