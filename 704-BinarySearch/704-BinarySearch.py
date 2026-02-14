# Last updated: 2/14/2026, 12:13:04 PM
1class Solution:
2    def uniqueOccurrences(self, arr: List[int]) -> bool:
3        nums = set()
4        occurances = set()
5        for num in arr:
6            if num not in nums:
7                occurances.add(arr.count(num))
8                nums.add(num)
9        if len(nums) == len(occurances):
10            return True
11        return False