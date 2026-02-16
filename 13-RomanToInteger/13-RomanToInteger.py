# Last updated: 2/15/2026, 8:54:26 PM
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {
            'I': 1,
            'V': 5, 
            'X': 10,
            'L': 50, 
            'C': 100, 
            'D': 500, 
            'M': 1000
        }
        total = 0
        prev = ''
        for i in range(0, len(s)):
            total += roman_dict[s[i]]
            if ((s[i] == 'V' or s[i] == 'X') and prev == 'I'):
                total -= 2
            elif ((s[i] == 'L' or s[i] == 'C') and prev == 'X'):
                total -= 20
            elif ((s[i] == 'D' or s[i] == 'M') and prev == 'C'):
                total -= 200
            prev = s[i]
        return total