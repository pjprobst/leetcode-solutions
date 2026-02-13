# Last updated: 2/13/2026, 6:15:47 PM
1class Solution:
2    def search(self, nums: List[int], target: int) -> int:
3        low = 0
4        high = len(nums)-1
5        while low <= high:
6            mid = int(low + (high - low) / 2)
7            if nums[mid] == target:
8                return mid
9            elif nums[mid] > target:
10                high = mid -1
11            else:
12                low = mid +1
13        return -1