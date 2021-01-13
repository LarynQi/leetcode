# https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

# https://leetcode.com/submissions/detail/442338282/
# 01/12/2021 21:37  

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        n = len(piles) // 3
        count = 0
        i = 0
        total = 0
        while count < n:
            total += piles[i + 1]
            count += 1
            i += 2
        return total