# Last updated: 2/17/2026, 3:19:18 PM
1class Solution:
2    def generate(self, numRows: int) -> List[List[int]]:
3        '''
4                1
5               1 1
6              1 2 1
7             1 3 3 1
8            1 4 6 4 1
9          1 5 10 10 5 1
10         1 6 15 20 15 6 1
11
12        '''
13        res = []
14        for i in range(numRows):
15            row = []
16            for j in range(i+1):
17                if i == 0:
18                    row.append(1)
19                elif j-1 in range(len(res[i-1])) and j in range(len(res[i-1])):
20                    row.append(res[i-1][j-1] + res[i-1][j])
21                else:
22                    row.append(1)
23            res.append(row)
24        return res