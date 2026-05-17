# Last updated: 5/16/2026, 8:48:44 PM
1class Solution:
2    def maximumXor(self, s: str, t: str) -> str:
3        tcount = t.count("1")
4        res = list(s)
5        for i in range(len(res)):
6            if s[i] == "0" and tcount:
7                res[i] = "1"
8                tcount -= 1
9        j = len(s)-1
10        while tcount:
11            if s[j] == "1":
12                res[j] = "0"
13                tcount -= 1
14            j -= 1
15        return("".join(res))