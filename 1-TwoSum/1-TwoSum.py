# Last updated: 2/16/2026, 7:34:54 PM
1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        seen = {}
4        for i in range(0, len(nums)):
5            if target-nums[i] in seen:
6                return [seen[target-nums[i]], i]
7            seen[nums[i]] = i