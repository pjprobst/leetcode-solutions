# Last updated: 3/5/2026, 12:11:57 PM
1class Solution:
2    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
3        occ = []
4        for i in range(len(nums)):
5            if nums[i] == x:
6                occ.append(i)
7        print(occ)
8        ans = []
9        for query in queries:
10            if query not in range(len(occ)+1):
11                ans.append(-1)
12            else:
13                ans.append(occ[query-1])
14        return ans