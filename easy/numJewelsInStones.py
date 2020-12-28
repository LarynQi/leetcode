# https://leetcode.com/problems/jewels-and-stones/

# https://leetcode.com/submissions/detail/268723634/
# 10/10/2019 13:51  

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        for stone in S:
            for jewel in J:
                if stone == jewel:
                    count += 1
        return count