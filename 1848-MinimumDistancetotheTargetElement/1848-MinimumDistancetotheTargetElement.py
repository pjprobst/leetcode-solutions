# Last updated: 4/14/2026, 4:38:56 PM
1class Solution:
2    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
3        mini = len(nums)
4        for i in range(len(nums)):
5            if nums[i] == target:
6                mini = min(mini, abs(i-start))
7        return mini