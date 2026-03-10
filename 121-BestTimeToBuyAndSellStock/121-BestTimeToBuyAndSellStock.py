# Last updated: 3/10/2026, 5:52:11 PM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprof = 0
        minprice = prices[0]

        for price in prices[1:]:
            maxprof = max(maxprof, price - minprice)
            minprice = min(minprice, price)
        return maxprof