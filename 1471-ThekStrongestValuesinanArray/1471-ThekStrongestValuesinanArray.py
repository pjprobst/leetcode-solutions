# Last updated: 2/18/2026, 7:50:49 PM
1class Solution:
2    def buildArray(self, nums: List[int]) -> List[int]:
3        ans = [0] * len(nums)
4        for i in range(len(nums)):
5            ans[i] = nums[nums[i]]
6        return ans