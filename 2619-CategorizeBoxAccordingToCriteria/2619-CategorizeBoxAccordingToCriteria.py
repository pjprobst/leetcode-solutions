# Last updated: 2/25/2026, 3:35:38 PM
class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        res = ""
        volume = length * width * height
        if length >= pow(10, 4) or width >= pow(10, 4) or height >= pow(10, 4) or volume >= pow(10, 9):
            res += "Bulky"
            if mass >= 100:
                res += "Heavy"
        elif mass >= 100:
            res += "Heavy"
        else:
            res = "Neither"
        
        if res == "BulkyHeavy":
            return "Both"
        return res
