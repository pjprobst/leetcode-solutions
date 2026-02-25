# Last updated: 2/25/2026, 3:35:37 PM
class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        total = 0
        addk = 0
        subk = 0

        if k == 0:
            if nums1 != nums2:
                return -1
            else:
                return 0

        for i in range(len(nums1)):
            num1 = nums1[i]
            num2 =nums2[i]
            if num2 - num1 < 0:
                subk += abs((num2 - num1)/k)
            elif num2 - num1 > 0:
                addk += (num2 - num1)/k
            total += (num2 - num1)/k
            if subk % 1 != 0 or addk % 1 != 0:
                return -1
        if total != 0 or subk != addk or subk % 1 != 0:
            return -1
        else:
            return int(subk)
        
