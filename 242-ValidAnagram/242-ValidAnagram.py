# Last updated: 2/16/2026, 9:58:13 PM
1class Solution:
2    def isAnagram(self, s: str, t: str) -> bool:
3        if len(t) != len(s):
4            return False
5        seen = {}
6        for l in s:
7            if l in seen:
8                seen[l] = seen[l] + 1
9            else:
10                seen[l] = 1
11        print(seen)
12        tset = set(t)
13        print(tset)
14        for l in tset:
15            if l not in seen:
16                return False
17            if t.count(str(l)) != seen[l]:
18                return False
19        return True