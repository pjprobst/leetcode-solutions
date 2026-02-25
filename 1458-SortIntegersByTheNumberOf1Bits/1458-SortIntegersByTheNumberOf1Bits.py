# Last updated: 2/25/2026, 3:35:49 PM
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr = sorted(arr)
        binarr = [[0,0]] * len(arr)
        for i, num in enumerate(arr):
            binarr[i] = [i, bin(num).count("1")]
        binarr = sorted(binarr, key= lambda x: x[1])
        res = [0] * len(arr)
        for k, j in enumerate(binarr):
            res[k] = arr[j[0]]
        return res

