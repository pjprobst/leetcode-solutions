# Last updated: 3/10/2026, 5:51:54 PM
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        count = None
        for i in range(len(nums)):
            if count is None and nums[i] is 1:
                count = 0
            elif nums[i] is 1 and count is not None:
                if count < k:
                    return False
                count = 0
            elif nums[i] is 0 and count is not None:
                count += 1
        return True