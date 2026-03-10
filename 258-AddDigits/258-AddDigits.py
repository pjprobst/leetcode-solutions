# Last updated: 3/10/2026, 5:52:05 PM
class Solution:
    def addDigits(self, num: int) -> int:
        num = str(num)
        total = 0
        for l in num:
            total += int(l)
        
        if total < 10:
            return total
        res = None
        while res is None:
            res = self.addDigits(total)
        return res