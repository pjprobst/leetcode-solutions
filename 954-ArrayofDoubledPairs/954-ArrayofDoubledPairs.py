# Last updated: 2/19/2026, 1:17:18 PM
1class Solution:
2    def singleNumber(self, nums: List[int]) -> int:
3        seen = set()
4        for num in nums:
5            if num in seen:
6                seen.remove(num)
7            else:
8                seen.add(num)
9        return seen.pop()