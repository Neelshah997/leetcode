class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr = float('inf')
        profit = 0
        for i in range(len(prices)):
            if(curr>prices[i]):
                curr = prices[i]
            elif(profit<prices[i]-curr):
                profit = prices[i]-curr
        return profit