# Last updated: 2/25/2026, 3:35:52 PM
class Solution:
    def binaryGap(self, n: int) -> int:
        max_distance = 0
        count = 0
        for num in bin(n)[2:]:
            if count != 0 and num == '1':
                max_distance = max(max_distance, count)
                count = 0
            if count == 0 and num == '1':
                count += 1
            elif count != 0 and num == '0':
                count += 1
        return max_distance