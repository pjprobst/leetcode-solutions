# Last updated: 2/15/2026, 8:54:25 PM
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        print(nums)
        if (len(nums) % 2 == 0):
            return (nums[len(nums)//2 - 1] + nums[len(nums)//2])/2
        else:
            return float(nums[len(nums)//2])        