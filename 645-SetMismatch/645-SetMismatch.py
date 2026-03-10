# Last updated: 3/10/2026, 5:52:01 PM
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dupl = 0
        miss = 0
        for i in range(1, len(nums)+1):
            if i not in nums:
                miss = i
            if nums.count(i) > 1:
                dupl = i
            if miss != 0 and dupl != 0:
                break
        return [dupl, miss]
