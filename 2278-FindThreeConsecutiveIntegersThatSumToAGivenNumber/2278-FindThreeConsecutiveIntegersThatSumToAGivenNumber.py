# Last updated: 3/10/2026, 5:51:44 PM
class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num % 3 == 0:
            return [num //3 -1, num // 3, num //3 +1]
        else:
            return []