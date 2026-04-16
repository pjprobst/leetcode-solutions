# Last updated: 4/16/2026, 3:27:48 PM
1class Solution:
2    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
3        res = []
4        mapd = dict()
5        for i in range(len(nums)):
6            if nums[i] not in mapd:
7                mapd[nums[i]] = [i]
8            else:
9                mapd[nums[i]].append(i)
10
11        for q in queries:
12            mini = -1
13            if nums[q] in mapd and len(mapd[nums[q]]) > 1:
14                pos = self.bisect_left(mapd[nums[q]], q)
15                l = mapd[nums[q]][(pos - 1) % len(mapd[nums[q]])]
16                r = mapd[nums[q]][(pos + 1) % len(mapd[nums[q]])]
17                mini = min(abs(q-l), abs(len(nums)-q + l), abs(len(nums)-l + q), abs(q-r), abs(len(nums)-q + r), abs(len(nums)-r + q))
18            res.append(mini)         
19        return res
20    
21    def bisect_left(self, arr, target) -> int:
22        lo, hi = 0, len(arr)
23        while lo < hi:
24            mid = (lo + hi) // 2
25            if arr[mid] < target:
26                lo = mid + 1
27            else:
28                hi = mid
29        return lo