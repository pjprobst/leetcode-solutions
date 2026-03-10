# Last updated: 3/10/2026, 5:51:39 PM
class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        occ = []
        for i in range(len(nums)):
            if nums[i] == x:
                occ.append(i)
        ans = []
        for query in queries:
            if query not in range(len(occ)+1):
                ans.append(-1)
            else:
                ans.append(occ[query-1])
        return ans