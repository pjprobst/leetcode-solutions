# Last updated: 2/25/2026, 3:35:48 PM
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        my_dict = {}
        sorted_nums = sorted(nums)
        count = 0
        for num in sorted_nums:
            if num not in my_dict:
                my_dict[num] = count
            count += 1
        res = []
        for num in nums:
            res.append(my_dict.get(num))
        return res