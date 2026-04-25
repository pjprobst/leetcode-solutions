# Last updated: 4/24/2026, 8:44:59 PM
1class Solution:
2    def furthestDistanceFromOrigin(self, moves: str) -> int:
3        lcount, rcount, count = 0,0,0
4        for move in moves:
5            if move == 'L':
6                lcount += 1
7            elif move == 'R':
8                rcount += 1
9            else:
10                count += 1
11        return count + abs(lcount - rcount)