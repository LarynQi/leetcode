# https://leetcode.com/problems/last-stone-weight/

# https://leetcode.com/submissions/detail/440532147/
# 01/08/2021 20:10  

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        ### Brute Force ###
        stones.sort(reverse=True)
        while stones and len(stones) > 1:
            # print(stones)
            y, x = stones[0], stones[1]
            new = y - x
            stones.pop(1)
            if new == 0:
                stones.pop(0)
            else:
                stones[0] = new
                i = 0
                while i < len(stones) - 1:
                    if stones[i] < stones[i + 1]:
                        stones[i], stones[i + 1] = stones[i + 1], stones[i]
                        i += 1
                    else:
                        break
        return sum(stones)