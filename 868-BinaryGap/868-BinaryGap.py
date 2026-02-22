# Last updated: 2/22/2026, 12:50:22 AM
1class Solution:
2    def binaryGap(self, n: int) -> int:
3        max_distance = 0
4        count = 0
5        for num in bin(n)[2:]:
6            if count != 0 and num == '1':
7                max_distance = max(max_distance, count)
8                count = 0
9            if count == 0 and num == '1':
10                count += 1
11            elif count != 0 and num == '0':
12                count += 1
13        return max_distance