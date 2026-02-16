# Last updated: 2/16/2026, 12:16:25 PM
1class Solution:
2    def getConcatenation(self, nums: List[int]) -> List[int]:
3        res = []
4        for i in range(0, (len(nums))*2):
5            if i > len(nums)-1:
6                res.append(nums[i-(len(nums))])
7            else:
8                res.append(nums[i])
9        return res