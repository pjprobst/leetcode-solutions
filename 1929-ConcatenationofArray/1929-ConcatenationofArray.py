# Last updated: 2/16/2026, 12:20:45 PM
1class Solution:
2    def shuffle(self, nums: List[int], n: int) -> List[int]:
3        pointer_one = 0
4        pointer_two = n
5        res = []
6        while len(res) < len(nums):
7            res.append(nums[pointer_one])
8            res.append(nums[pointer_two])
9            pointer_one += 1
10            pointer_two += 1
11        return res