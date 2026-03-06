# Last updated: 3/5/2026, 7:10:05 PM
1class Solution:
2    def checkOnesSegment(self, s: str) -> bool:
3        for i in range(len(s)):
4            if s[i] == "0":
5                if s[i:].count("1") >= 1:
6                    return False
7                else:
8                    return True
9        return True