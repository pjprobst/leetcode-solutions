# Last updated: 3/10/2026, 5:52:07 PM
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        seen = set()
        islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in seen:
                    islands += 1
                    q = collections.deque()
                    q.append((r,c))
                    seen.add((r,c))
                    while q:
                        row, col = q.popleft()
                        directions = [[row+1,col], [row-1,col], [row,col+1],[row,col-1]]
                        for dr,dc in directions:
                            if dr in range(rows) and dc in range(cols) and grid[dr][dc] == "1" and (dr,dc) not in seen:
                                seen.add((dr,dc))
                                q.append((dr,dc))
        return islands
                    
                        