# Last updated: 2/15/2026, 8:54:12 PM
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        seen = []
        lsum = 0
        i = 0
        while i != len(mat):
            lsum += mat[i][i]
            seen.append([i,i])
            i += 1

        rsum = 0
        j = 0
        while j != len(mat):
            if [j, len(mat[j]) - 1 - j] not in seen:
                rsum += mat[j][len(mat[j]) - 1 - j]
                seen.append([j, len(mat[j]) - 1 - j])
            j += 1
        return lsum + rsum