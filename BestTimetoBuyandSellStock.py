from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_p= float("inf")
        max_profit = 0
        for i in range(len(prices)):
            if min_p > prices[i]:
                min_p = prices[i]
            if max_profit < prices[i] - min_p:
                max_profit = prices[i] - min_p
        return max_profit          