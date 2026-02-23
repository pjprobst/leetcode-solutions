# Last updated: 2/23/2026, 12:57:04 AM
1class Solution:
2    def hasAllCodes(self, s: str, k: int) -> bool:
3        seen = set()
4        for i in range(len(s)-k+1):
5            seen.add(s[i:i+k])
6        if k == 1 and len(seen) == 2:
7            return True
8        elif len(seen) != math.pow(2, k):
9            return False
10        return True