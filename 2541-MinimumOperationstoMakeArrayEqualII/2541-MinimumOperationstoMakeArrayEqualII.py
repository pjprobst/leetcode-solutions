# Last updated: 2/17/2026, 3:02:08 PM
1class Solution:
2    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
3        total = 0
4        addk = 0
5        subk = 0
6
7        if k == 0 and nums1 != nums2:
8            return -1
9        elif nums1 == nums2:
10            return 0
11
12        for i in range(len(nums1)):
13            num1 = nums1[i]
14            num2 =nums2[i]
15            if num2 - num1 < 0:
16                print("-", abs((num2 - num1)/k))
17                subk += abs((num2 - num1)/k)
18            elif num2 - num1 > 0:
19                print("+", (num2 - num1)/k)
20                addk += (num2 - num1)/k
21            total += (num2 - num1)/k
22            if subk % 1 != 0 or addk % 1 != 0:
23                return -1
24        print(total)
25        print(addk)
26        print(subk)
27        if total != 0 or subk != addk or subk % 1 != 0:
28            return -1
29        else:
30            return int(subk)
31        
32