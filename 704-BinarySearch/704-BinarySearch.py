# Last updated: 2/14/2026, 2:02:43 PM
1class Solution:
2    def canBeIncreasing(self, nums: List[int]) -> bool:
3        if len(nums) == 2:
4            return True
5        for i in range(0, len(nums)):
6            if i == 0:
7                if self.isSorted(nums[1:len(nums)]):
8                    return True
9            elif i == len(nums):
10                if self.isSorted(nums[0:len(nums)]):
11                    return True
12            else:
13                if self.isSorted(nums[0:i] + nums[i+1:len(nums)]):
14                    return True    
15        return False
16        
17    def isSorted(self, nums: List[int]) -> bool:
18        sorted_nums = sorted(nums)
19        set_nums = set(nums)
20        if nums == sorted_nums and (nums.count(nums[0]) != len(nums)) and len(set_nums) == len(nums):
21            return True
22        return False
23