# Last updated: 2/15/2026, 8:54:06 PM
class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        have1 = 0
        have2 = 0
        cost = 0
        while (have1 < need1) or (have2 < need2):
            if have1 < need1 and not (have2 < need2):
                if costBoth >= cost1:
                    cost += cost1 * (need1-have1)
                    have1 += need1-have1
                else:
                    cost += costBoth * (need1-have1)
                    have1 += need1-have1
                    have2 += need2-have2
            elif have2 < need2 and not (have1 < need1):
                if costBoth >= cost2:
                    cost += cost2 * (need2-have2)
                    have2 += need2-have2
                else:
                    cost += costBoth * (need2-have2)
                    have1 += need2-have2
                    have2 += need2-have2
            else:
                if costBoth < cost1+cost2:
                    have1 += min(need1,need2)
                    have2 += min(need1,need2)
                    cost += costBoth * min(need1,need2)
                else:
                    have1 += min(need1,need2)
                    have2 += min(need1,need2)
                    cost += (cost1+cost2) * min(need1,need2)
        return cost