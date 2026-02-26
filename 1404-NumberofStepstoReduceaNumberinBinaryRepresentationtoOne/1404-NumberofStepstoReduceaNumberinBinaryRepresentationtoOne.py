# Last updated: 2/25/2026, 8:11:19 PM
1class Solution:
2    def kLengthApart(self, nums: List[int], k: int) -> bool:
3        count = None
4        for i in range(len(nums)):
5            if count is None and nums[i] is 1:
6                count = 0
7            elif nums[i] is 1 and count is not None:
8                if count < k:
9                    return False
10                count = 0
11            elif nums[i] is 0 and count is not None:
12                count += 1
13        return True