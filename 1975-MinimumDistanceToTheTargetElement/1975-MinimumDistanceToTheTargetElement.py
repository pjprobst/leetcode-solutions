# Last updated: 4/24/2026, 8:45:31 PM
class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        mini = len(nums)
        for i in range(len(nums)):
            if nums[i] == target and mini > abs(i-start):
                mini = abs(i-start)
        return mini