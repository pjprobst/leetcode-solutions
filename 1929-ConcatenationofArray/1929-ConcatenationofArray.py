# Last updated: 2/16/2026, 2:32:56 PM
1class Solution:
2    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
3        my_dict = {}
4        sorted_nums = sorted(nums)
5        count = 0
6        for num in sorted_nums:
7            if num not in my_dict:
8                my_dict[num] = count
9            count += 1
10        res = []
11        for num in nums:
12            res.append(my_dict.get(num))
13        return res