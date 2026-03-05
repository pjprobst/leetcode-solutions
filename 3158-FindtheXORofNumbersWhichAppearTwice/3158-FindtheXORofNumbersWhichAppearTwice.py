# Last updated: 3/5/2026, 12:12:06 PM
1class Solution:
2    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
3        occ = []
4        for i in range(len(nums)):
5            if nums[i] == x:
6                occ.append(i)
7        ans = []
8        for query in queries:
9            if query not in range(len(occ)+1):
10                ans.append(-1)
11            else:
12                ans.append(occ[query-1])
13        return ans