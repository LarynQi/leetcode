# https://leetcode.com/problems/frog-jump/

# https://leetcode.com/submissions/detail/427924487/
# 12/06/2020 12:51  
# Time Limit Exceeded

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[len(stones) - 1] > 9999:
            return False
        def helper(stones, k, prev):
            if len(stones) == 1:
                if stones[0] - prev == k - 1 or stones[0] - prev == k or stones[0] - prev == k + 1:
                    return True
                return False
            if prev == 0:
                if stones[0] != 1:
                    return False
                return helper(stones[1:], 1, 1)
            if stones[0] - prev > k + 1:
                return False
            if stones[0] - prev == k + 1:
                return helper(stones[1:], stones[0] - prev, stones[0])
            if stones[0] - prev == k - 1 or stones[0] - prev == k:
                return helper(stones[1:], stones[0] - prev, stones[0]) or helper(stones[1:], k, prev)
            return helper(stones[1:], k, prev)
        return helper(stones[1:], 0, 0)