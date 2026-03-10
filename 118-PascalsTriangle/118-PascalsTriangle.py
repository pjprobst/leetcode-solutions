# Last updated: 3/10/2026, 5:52:12 PM
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        '''
                1
               1 1
              1 2 1
             1 3 3 1
            1 4 6 4 1
          1 5 10 10 5 1
         1 6 15 20 15 6 1

        '''
        res = []
        for i in range(numRows):
            row = []
            for j in range(i+1):
                if i == 0:
                    row.append(1)
                elif j-1 in range(len(res[i-1])) and j in range(len(res[i-1])):
                    row.append(res[i-1][j-1] + res[i-1][j])
                else:
                    row.append(1)
            res.append(row)
        return res