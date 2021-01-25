# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# https://leetcode.com/interview/reports/SW50ZXJ2aWV3U2Vzc2lvbk5vZGU6MTUwNTI4Ng==

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # loop through arr
        # if you find an increasing pair of elements, save the smaller number
        # continuing looping and keep track of the highest value and return the difference between lowest and highest
        # lowest = None
        # highest = None
        # for i in range(len(prices)):
        #     if i + 1 < len(prices) and lowest is None:
        #         if prices[i] < prices[i + 1]:
        #             lowest = prices[i]
        #     else:
        #         if highest is None:
        #             highest = prices[i]
        #         else:
        #             highest = max(prices[i], highest)
        # if lowest is None:
        #     return 0
        # return highest - lowest
    
        # Brute force
        def helper(prices, low, best):
            if not prices:
                if best is None or low is None:
                    return 0
                return best - low
            if low is None:
                return helper(prices[1:], prices[0], best)
            elif prices[0] < low:
                return max(helper(prices[1:], prices[0], None), helper(prices[1:], low, best))
            elif best is None:
                return helper(prices[1:], low, prices[0])
            return max(helper(prices[1:], prices[0], 0), helper(prices[1:], low, max(best, prices[0])))
                
        return helper(prices, None, None)

### SOLUTION (AFTERWARDS) ###

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy = None
        profit = 0
        for p in prices:
            if min_buy is None:
                min_buy = p
            else:
                if p > min_buy:
                    profit = max(profit, p - min_buy)
                else:
                    min_buy = p
        return profit