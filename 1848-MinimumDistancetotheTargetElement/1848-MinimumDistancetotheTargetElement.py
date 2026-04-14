# Last updated: 4/14/2026, 4:39:35 PM
1class Solution:
2    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
3        mini = len(nums)
4        for i in range(len(nums)):
5            if nums[i] == target and mini > abs(i-start):
6                mini = abs(i-start)
7        return mini