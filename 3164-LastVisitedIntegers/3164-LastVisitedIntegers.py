# Last updated: 3/10/2026, 5:51:40 PM
class Solution:
    def lastVisitedIntegers(self, nums: List[int]) -> List[int]:
        seen = []
        ans = []
        k = 0
        for num in nums:
            if num < 0:
                k += 1
                if k-1 <= len(seen)-1:
                    ans.append(seen[k-1])
                else:
                    ans.append(-1)
            else:
                k = 0
                seen.insert(0,num)
        return ans