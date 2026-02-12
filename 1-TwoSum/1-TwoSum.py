# Last updated: 2/12/2026, 3:41:11 PM
1class Solution:
2    def romanToInt(self, s: str) -> int:
3        roman_dict = {
4            'I': 1,
5            'V': 5, 
6            'X': 10,
7            'L': 50, 
8            'C': 100, 
9            'D': 500, 
10            'M': 1000
11        }
12        total = 0
13        prev = ''
14        for i in range(0, len(s)):
15            total += roman_dict[s[i]]
16            if ((s[i] == 'V' or s[i] == 'X') and prev == 'I'):
17                total -= 2
18            elif ((s[i] == 'L' or s[i] == 'C') and prev == 'X'):
19                total -= 20
20            elif ((s[i] == 'D' or s[i] == 'M') and prev == 'C'):
21                total -= 200
22            prev = s[i]
23        return total