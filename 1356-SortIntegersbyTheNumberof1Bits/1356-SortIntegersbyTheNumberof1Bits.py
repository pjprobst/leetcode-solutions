# Last updated: 2/24/2026, 10:45:17 PM
1class Solution:
2    def sortByBits(self, arr: List[int]) -> List[int]:
3        arr = sorted(arr)
4        binarr = [[0,0]] * len(arr)
5        for i, num in enumerate(arr):
6            binarr[i] = [i, bin(num).count("1")]
7        binarr = sorted(binarr, key= lambda x: x[1])
8        res = [0] * len(arr)
9        for k, j in enumerate(binarr):
10            res[k] = arr[j[0]]
11        return res
12
13