# Last updated: 2/14/2026, 2:20:26 PM
1class Solution:
2    def diagonalSum(self, mat: List[List[int]]) -> int:
3        seen = []
4        lsum = 0
5        i = 0
6        while i != len(mat):
7            lsum += mat[i][i]
8            seen.append([i,i])
9            i += 1
10
11        rsum = 0
12        j = 0
13        while j != len(mat):
14            if [j, len(mat[j]) - 1 - j] not in seen:
15                rsum += mat[j][len(mat[j]) - 1 - j]
16                seen.append([j, len(mat[j]) - 1 - j])
17            j += 1
18        return lsum + rsum