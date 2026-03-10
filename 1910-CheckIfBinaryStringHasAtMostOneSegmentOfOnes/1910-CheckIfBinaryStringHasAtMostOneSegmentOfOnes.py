# Last updated: 3/10/2026, 5:51:47 PM
class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        for i in range(len(s)):
            if s[i] == "0":
                if s[i:].count("1") >= 1:
                    return False
                else:
                    return True
        return True