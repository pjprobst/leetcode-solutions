# Last updated: 3/10/2026, 5:52:04 PM
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        num_set = set(nums)
        res = []
        for i in range(1, len(nums)+1):
            if i not in num_set:
                res.append(i)
        return res