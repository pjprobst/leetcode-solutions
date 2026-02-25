# Last updated: 2/25/2026, 3:35:44 PM
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        pointer_one = 0
        pointer_two = n
        res = []
        while len(res) < len(nums):
            res.append(nums[pointer_one])
            res.append(nums[pointer_two])
            pointer_one += 1
            pointer_two += 1
        return res