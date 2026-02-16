# Last updated: 2/15/2026, 8:54:11 PM
class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        if len(nums) == 2:
            return True
        for i in range(0, len(nums)):
            if i == 0:
                if self.isSorted(nums[1:len(nums)]):
                    return True
            elif i == len(nums):
                if self.isSorted(nums[0:len(nums)]):
                    return True
            else:
                if self.isSorted(nums[0:i] + nums[i+1:len(nums)]):
                    return True    
        return False
        
    def isSorted(self, nums: List[int]) -> bool:
        sorted_nums = sorted(nums)
        set_nums = set(nums)
        if nums == sorted_nums and (nums.count(nums[0]) != len(nums)) and len(set_nums) == len(nums):
            return True
        return False
