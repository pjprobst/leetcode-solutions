# Last updated: 4/16/2026, 3:38:13 PM
1class Solution:
2    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
3        res = []
4        mapd = {}
5        loc = {} 
6
7        qset = set(queries)
8        for i in range(len(nums)):
9            if nums[i] not in mapd:
10                mapd[nums[i]] = [i]
11                if i in qset:
12                    loc[i] = 0
13            else:
14                if i in qset:
15                    loc[i] = len(mapd[nums[i]]) 
16                mapd[nums[i]].append(i)
17
18        n = len(nums)
19        for q in queries:
20            mini = -1
21            positions = mapd[nums[q]]
22            if len(positions) > 1:
23                pos = loc[q]
24                l = positions[(pos - 1) % len(positions)]
25                r = positions[(pos + 1) % len(positions)]
26                mini = min(
27                    abs(q-l), abs(n-q+l), abs(n-l+q),
28                    abs(q-r), abs(n-q+r), abs(n-r+q)
29                )
30            res.append(mini)
31
32        return res