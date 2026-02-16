# Last updated: 2/15/2026, 8:54:14 PM
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        nums = set()
        occurances = set()
        for num in arr:
            if num not in nums:
                occurances.add(arr.count(num))
                nums.add(num)
        if len(nums) == len(occurances):
            return True
        return False