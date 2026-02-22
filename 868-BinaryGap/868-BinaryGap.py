# Last updated: 2/22/2026, 12:50:17 AM
1class Solution:
2    def binaryGap(self, n: int) -> int:
3        max_distance = 0
4        count = 0
5        print(bin(n)[2:])
6        for num in bin(n)[2:]:
7            if count != 0 and num == '1':
8                max_distance = max(max_distance, count)
9                count = 0
10            if count == 0 and num == '1':
11                count += 1
12            elif count != 0 and num == '0':
13                count += 1
14        return max_distance