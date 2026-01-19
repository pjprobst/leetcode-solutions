// Last updated: 1/19/2026, 3:16:06 PM
1class Solution {
2    public int maxSideLength(int[][] mat, int threshold) {
3        int[][] prefix = new int[mat.length + 1][mat[0].length + 1]; 
4        for (int i = 1; i <= mat.length; i++){
5            for (int j = 1; j <= mat[0].length; j++){
6                prefix[i][j] = prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1] + mat[i-1][j-1];
7            }
8        }
9        int maxSize = Math.min(mat.length, mat[0].length);
10        for (int size = maxSize; size >= 1; size--){
11            for (int row = 0; row <= mat.length - size; row++){
12                for (int col = 0; col <= mat[0].length - size; col++){
13                    int r2 = row + size;
14                    int c2 = col + size;
15                    int sum = prefix[r2][c2] - prefix[row][c2] - prefix[r2][col] + prefix[row][col];
16                    
17                    if (sum <= threshold) {
18                        return size;
19                    }
20                }
21            }
22        }
23        return 0;
24    }
25}