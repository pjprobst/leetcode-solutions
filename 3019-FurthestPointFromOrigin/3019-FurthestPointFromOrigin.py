# Last updated: 4/24/2026, 8:45:25 PM
class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        lcount, rcount, count = 0,0,0
        for move in moves:
            if move == 'L':
                lcount += 1
            elif move == 'R':
                rcount += 1
            else:
                count += 1
        return count + abs(lcount - rcount)