# Last updated: 2/19/2026, 12:34:23 AM
1class Solution:
2    def sortByReflection(self, nums: List[int]) -> List[int]:
3        binnums = []
4        for i in range(len(nums)):
5            binnum = bin(nums[i])[::-1]
6            binnums.append([int(binnum[:len(binnum)-2], 2), nums[i]])
7        binnums = sorted(binnums)
8        print(binnums)
9
10        res = []
11        for i in range(len(binnums)):
12            res.append(binnums[i][1])
13        return res