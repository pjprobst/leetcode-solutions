# Last updated: 3/3/2026, 5:49:12 PM
1class Solution:
2    def sumOfThree(self, num: int) -> List[int]:
3        if num % 3 == 0:
4            return [num //3 -1, num // 3, num //3 +1]
5        else:
6            return []