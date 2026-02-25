# Last updated: 2/25/2026, 3:35:38 PM
class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums = sorted(nums)
        l = 0
        r = len(nums)-1
        res = set()
        while l in range(len(nums)) and r in range(len(nums)):
            res.add((nums[l] + nums[r]) / 2)
            l += 1
            r -= 1
        return len(res)