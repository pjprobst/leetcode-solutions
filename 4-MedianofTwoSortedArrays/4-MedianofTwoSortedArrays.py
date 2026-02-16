# Last updated: 2/15/2026, 8:53:44 PM
1class Solution:
2    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
3        nums = nums1 + nums2
4        nums.sort()
5        print(nums)
6        if (len(nums) % 2 == 0):
7            return (nums[len(nums)//2 - 1] + nums[len(nums)//2])/2
8        else:
9            return float(nums[len(nums)//2])        