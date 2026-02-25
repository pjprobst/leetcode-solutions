# Last updated: 2/24/2026, 10:41:44 PM
1class Solution:
2    def sortByBits(self, arr: List[int]) -> List[int]:
3        arr = sorted(arr)
4        binarr = []
5        for i, num in enumerate(arr):
6            binarr.append([i, bin(num).count("1")])
7        binarr = sorted(binarr, key= lambda x: x[1])
8        res = []
9        for j in binarr:
10            res.append(arr[j[0]])
11        return res
12
13