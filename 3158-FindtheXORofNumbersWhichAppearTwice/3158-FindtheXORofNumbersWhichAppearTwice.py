# Last updated: 3/5/2026, 12:03:37 PM
1class Solution:
2    def duplicateNumbersXOR(self, nums: List[int]) -> int:
3        seen = set()
4        pairs = []
5        for num in nums:
6            if num in seen:
7                pairs.append(num)
8            else:
9                seen.add(num)
10        if not pairs:
11            return 0
12        total = pairs[0]
13        print(pairs)
14        for i in range(1, len(pairs)):
15            print(total)
16            total = total ^ pairs[i]
17        return total
18