# https://leetcode.com/problems/min-cost-climbing-stairs/

# https://leetcode.com/submissions/detail/440514056/
# 01/08/2021 19:07  

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        ### Need DP ###
        
        ### Tree Recursion: Time Limit Exceeded ###
        if not cost:
            return 0
        if len(cost) == 1:
            # return cost[0]
            return 0
        return min(cost[0] + self.minCostClimbingStairs(cost[1:]), cost[1] + self.minCostClimbingStairs(cost[2:]))