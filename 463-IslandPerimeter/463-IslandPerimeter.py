# Last updated: 2/17/2026, 1:02:25 AM
1class Solution:
2    def islandPerimeter(self, grid: List[List[int]]) -> int:
3        rows = len(grid)
4        cols = len(grid[0])
5        seen = set()
6        start = ""
7        res = 0
8        for r in range(rows):
9            for c in range(cols):
10                if grid[r][c] == 1:
11                    start = (r,c)
12                    break
13
14        q = collections.deque()
15        q.append(start)
16        seen.add(start)
17        while q:
18            row, col = q.popleft()
19            directions = [[row+1, col], [row-1, col], [row, col+1], [row, col-1]]
20            perimeter = 4
21            for dr, dc in directions:
22                if dr in range(rows) and dc in range(cols) and grid[dr][dc] == 1:
23                    if (dr,dc) not in seen:
24                        q.append((dr,dc))
25                        seen.add((dr,dc))
26                    perimeter -= 1
27            res += perimeter
28        return res