// Last updated: 2/15/2026, 8:54:14 PM
class Solution {
    public int maxSideLength(int[][] mat, int threshold) {
        int[][] prefix = new int[mat.length + 1][mat[0].length + 1]; 
        for (int i = 1; i <= mat.length; i++){
            for (int j = 1; j <= mat[0].length; j++){
                prefix[i][j] = prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1] + mat[i-1][j-1];
            }
        }
        int maxSize = Math.min(mat.length, mat[0].length);
        for (int size = maxSize; size >= 1; size--){
            for (int row = 0; row <= mat.length - size; row++){
                for (int col = 0; col <= mat[0].length - size; col++){
                    int r2 = row + size;
                    int c2 = col + size;
                    int sum = prefix[r2][c2] - prefix[row][c2] - prefix[r2][col] + prefix[row][col];
                    
                    if (sum <= threshold) {
                        return size;
                    }
                }
            }
        }
        return 0;
    }
}