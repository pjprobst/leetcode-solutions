# Last updated: 2/17/2026, 12:44:52 AM
1class Solution:
2    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
3        seen = set()
4        rows, cols = len(image), len(image[0])
5        tc = image[sr][sc]
6        q = collections.deque()
7        seen.add((sr,sc))
8        q.append((sr,sc))
9        while q:
10            row, col = q.popleft()
11            image[row][col] = color
12            directions = [[1+row, col], [row-1, col], [row,col+1], [row, col-1]]
13            for dr, dc in directions:
14                if (dr in range(rows) and dc in range(cols) and image[dr][dc] == tc and (dr, dc) not in seen):
15                    q.append((dr,dc))
16                    seen.add((dr,dc))
17        return image         