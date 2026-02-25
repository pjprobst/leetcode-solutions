# Last updated: 2/25/2026, 3:35:47 PM
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        nums_set = set(target)
        count = 0
        for i in range(1, n+1):
            if i in nums_set:
                res.append("Push")
                count += 1
            else:
                res.append("Push")
                res.append("Pop")
            if count == len(target):
                break
        return res