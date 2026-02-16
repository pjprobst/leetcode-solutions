# Last updated: 2/16/2026, 12:23:33 PM
1class Solution:
2    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
3        count = 0
4        max_count = 0
5        for num in nums:
6            if num:
7                count += 1
8            else:
9                max_count = max(max_count, count)
10                count = 0
11        max_count = max(max_count, count)
12        return max_count