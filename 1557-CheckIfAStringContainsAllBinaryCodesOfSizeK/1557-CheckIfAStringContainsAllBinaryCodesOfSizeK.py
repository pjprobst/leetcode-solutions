# Last updated: 2/25/2026, 3:35:45 PM
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        seen = set()
        for i in range(len(s)-k+1):
            seen.add(s[i:i+k])
        if k == 1 and len(seen) == 2:
            return True
        elif len(seen) != math.pow(2, k):
            return False
        return True