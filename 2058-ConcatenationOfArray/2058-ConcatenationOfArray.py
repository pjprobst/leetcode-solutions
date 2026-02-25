# Last updated: 2/25/2026, 3:35:41 PM
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(0, (len(nums))*2):
            if i > len(nums)-1:
                res.append(nums[i-(len(nums))])
            else:
                res.append(nums[i])
        return res