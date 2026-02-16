# Last updated: 2/15/2026, 8:54:08 PM
class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        c = 0
        v = 0
        vowels = ['a', 'e', 'i', 'o', 'u']
        nonconst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        s = s.replace(' ', '')
        for char in s:
            if char in vowels:
                v += 1
            elif char not in nonconst:
                c += 1
        if c > 0:
            return v//c
        return 0