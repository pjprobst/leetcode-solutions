# Last updated: 2/16/2026, 2:38:50 PM
1class Solution:
2    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
3        num_set = set(nums)
4        res = []
5        for i in range(1, len(nums)+1):
6            if i not in num_set:
7                res.append(i)
8        return res