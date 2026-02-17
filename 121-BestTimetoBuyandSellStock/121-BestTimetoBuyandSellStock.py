# Last updated: 2/16/2026, 9:40:44 PM
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        maxprof = 0
4        minprice = prices[0]
5
6        for price in prices[1:]:
7            maxprof = max(maxprof, price - minprice)
8            minprice = min(minprice, price)
9        return maxprof