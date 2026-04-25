# Last updated: 4/24/2026, 8:45:21 PM
class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        res = []
        mapd = {}
        loc = {} 

        qset = set(queries)
        for i in range(len(nums)):
            if nums[i] not in mapd:
                mapd[nums[i]] = [i]
                if i in qset:
                    loc[i] = 0
            else:
                if i in qset:
                    loc[i] = len(mapd[nums[i]]) 
                mapd[nums[i]].append(i)

        n = len(nums)
        for q in queries:
            mini = -1
            positions = mapd[nums[q]]
            if len(positions) > 1:
                pos = loc[q]
                l = positions[(pos - 1) % len(positions)]
                r = positions[(pos + 1) % len(positions)]
                mini = min(
                    abs(q-l), abs(n-q+l), abs(n-l+q),
                    abs(q-r), abs(n-q+r), abs(n-r+q)
                )
            res.append(mini)

        return res