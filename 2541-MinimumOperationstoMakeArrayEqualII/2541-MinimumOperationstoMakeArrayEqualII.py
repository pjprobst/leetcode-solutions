# Last updated: 2/17/2026, 3:05:32 PM
1class Solution:
2    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
3        total = 0
4        addk = 0
5        subk = 0
6
7        if k == 0:
8            if nums1 != nums2:
9                return -1
10            else:
11                return 0
12
13        for i in range(len(nums1)):
14            num1 = nums1[i]
15            num2 =nums2[i]
16            if num2 - num1 < 0:
17                subk += abs((num2 - num1)/k)
18            elif num2 - num1 > 0:
19                addk += (num2 - num1)/k
20            total += (num2 - num1)/k
21            if subk % 1 != 0 or addk % 1 != 0:
22                return -1
23        if total != 0 or subk != addk or subk % 1 != 0:
24            return -1
25        else:
26            return int(subk)
27        
28