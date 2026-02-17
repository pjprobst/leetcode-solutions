# Last updated: 2/16/2026, 11:17:13 PM
1class Solution:
2    def search(self, nums: List[int], target: int) -> int:
3        low = 0
4        high = len(nums)-1
5        while low <= high:
6            mid = (high + low)//2
7            print(low, mid, high)
8            if nums[mid] < target:
9                low = mid + 1
10            elif nums[mid] > target:
11                high = mid -1
12            else:
13                return mid
14        return -1