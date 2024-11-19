'''
day 2 (index+1) = 1
day 1 (index+1) = 7

'''
class Solution:
    ''' solution'''
    def maxProfit(self, prices: list[int]) -> int:
        '''maxprofit'''
        profit = 0
        buy = prices[0]
        for _, val in enumerate(prices[1:]):
            if val > buy:
                profit = max(profit, val - buy)
            else:
                buy = val
        return profit

obj = Solution()
print(obj.maxProfit([3,8,1,4,7,5]))
