# Last updated: 2/14/2026, 7:04:06 PM
1class Solution:
2    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
3        have1 = 0
4        have2 = 0
5        cost = 0
6        while (have1 < need1) or (have2 < need2):
7            if have1 < need1 and not (have2 < need2):
8                if costBoth >= cost1:
9                    cost += cost1 * (need1-have1)
10                    have1 += need1-have1
11                else:
12                    cost += costBoth * (need1-have1)
13                    have1 += need1-have1
14                    have2 += need2-have2
15            elif have2 < need2 and not (have1 < need1):
16                if costBoth >= cost2:
17                    cost += cost2 * (need2-have2)
18                    have2 += need2-have2
19                else:
20                    cost += costBoth * (need2-have2)
21                    have1 += need2-have2
22                    have2 += need2-have2
23            else:
24                if costBoth < cost1+cost2:
25                    have1 += min(need1,need2)
26                    have2 += min(need1,need2)
27                    cost += costBoth * min(need1,need2)
28                else:
29                    have1 += min(need1,need2)
30                    have2 += min(need1,need2)
31                    cost += (cost1+cost2) * min(need1,need2)
32        return cost