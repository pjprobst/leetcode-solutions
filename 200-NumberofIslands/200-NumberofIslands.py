# Last updated: 2/17/2026, 7:56:41 PM
1class Solution:
2    def numIslands(self, grid: List[List[str]]) -> int:
3        rows, cols = len(grid), len(grid[0])
4        seen = set()
5        islands = 0
6        for r in range(rows):
7            for c in range(cols):
8                if grid[r][c] == "1" and (r,c) not in seen:
9                    islands += 1
10                    q = collections.deque()
11                    q.append((r,c))
12                    seen.add((r,c))
13                    while q:
14                        row, col = q.popleft()
15                        directions = [[row+1,col], [row-1,col], [row,col+1],[row,col-1]]
16                        for dr,dc in directions:
17                            if dr in range(rows) and dc in range(cols) and grid[dr][dc] == "1" and (dr,dc) not in seen:
18                                seen.add((dr,dc))
19                                q.append((dr,dc))
20        return islands
21                    
22                        