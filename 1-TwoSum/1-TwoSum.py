# Last updated: 2/12/2026, 3:15:31 PM
1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        for i in range(0, len(nums)):
4            for j in range(i+1, len(nums)):
5                if nums[i] + nums[j] == target:
6                    return [i,j]
7