# Last updated: 2/25/2026, 3:35:35 PM
class Solution:
    def sortByReflection(self, nums: List[int]) -> List[int]:
        binnums = []
        for i in range(len(nums)):
            binnum = bin(nums[i])[::-1]
            binnums.append([int(binnum[:len(binnum)-2], 2), nums[i]])
        binnums = sorted(binnums)
        print(binnums)

        res = []
        for i in range(len(binnums)):
            res.append(binnums[i][1])
        return res