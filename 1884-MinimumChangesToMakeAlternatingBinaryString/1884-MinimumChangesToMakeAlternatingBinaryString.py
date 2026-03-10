# Last updated: 3/10/2026, 5:51:48 PM
class Solution:
    def minOperations(self, s: str) -> int:
        if len(s) % 2 == 0:
            poss = "01" * (len(s)//2)
        else:
            poss = ("01" * (len(s)//2)) + "0"

        count = sum(1 for a, b in zip(s, poss) if a != b)

        return min(count, len(s) - count)