# Last updated: 2/16/2026, 12:06:02 PM
1class Solution:
2    def addBinary(self, a: str, b: str) -> str:
3        return str(bin(int(a, 2) + int(b, 2)))[2:]