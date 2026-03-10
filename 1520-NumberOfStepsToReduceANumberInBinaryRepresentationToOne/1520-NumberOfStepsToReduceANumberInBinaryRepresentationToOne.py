# Last updated: 3/10/2026, 5:51:55 PM
class Solution:
    def numSteps(self, s: str) -> int:
        count = 0
        num = self.binaryToInt(s)
        while num != 1:
            if num % 2 == 0:
                num = num // 2
            else:
                num += 1
            count += 1
        return count
    def binaryToInt(self, s: str) -> int:
        total = 0
        add = int(math.pow(2, len(s)-1))
        for l in s:
            if l == "1":
                total += add
            add = add // 2
        return total