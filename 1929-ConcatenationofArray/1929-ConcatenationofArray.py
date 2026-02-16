# Last updated: 2/16/2026, 12:35:38 PM
1class Solution:
2    def findErrorNums(self, nums: List[int]) -> List[int]:
3        dupl = 0
4        miss = 0
5        for i in range(1, len(nums)+1):
6            if i not in nums:
7                miss = i
8            if nums.count(i) > 1:
9                dupl = i
10            if miss != 0 and dupl != 0:
11                break
12        return [dupl, miss]
13