class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        buy = prices[0]
        for i, val in enumerate(prices[1:]):
            if val > buy:
                profit = max(profit, val - buy)
            else:
                buy = val
        return profit
    
obj = Solution()
print(obj.maxProfit([3,8,1,4,7,5]))

# [7,1,5,3,6,4]
'''
day 2 (index+1) = 1
day 1 (index+1) = 7

'''