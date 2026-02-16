# Last updated: 2/15/2026, 8:54:16 PM
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        while low <= high:
            mid = int(low + (high - low) / 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid -1
            else:
                low = mid +1
        return -1