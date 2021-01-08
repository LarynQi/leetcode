# https://leetcode.com/problems/coin-change/


# https://leetcode.com/submissions/detail/440258006/
# 01/08/2021 04:07  
# Time Limit Exceeded

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        ### Need DP ###
        
        ### Tree Recursion: Time Limit Exceeded ###
        
        if amount == 0:
            return 0
        if amount < 0:
            return -1
        arr = []
        for c in coins:
            curr = self.coinChange(coins, amount - c)
            if curr != -1:
                arr.append(curr)
        if not arr:
            return -1
        return 1 + min(arr)