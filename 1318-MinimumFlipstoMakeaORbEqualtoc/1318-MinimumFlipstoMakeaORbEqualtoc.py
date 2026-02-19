# Last updated: 2/19/2026, 10:12:57 AM
1class Solution:
2    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
3        res = ""
4        volume = length * width * height
5        if length >= pow(10, 4) or width >= pow(10, 4) or height >= pow(10, 4) or volume >= pow(10, 9):
6            res += "Bulky"
7            if mass >= 100:
8                res += "Heavy"
9        elif mass >= 100:
10            res += "Heavy"
11        else:
12            res = "Neither"
13        
14        if res == "BulkyHeavy":
15            return "Both"
16        return res
17