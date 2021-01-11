# https://leetcode.com/problems/count-of-matches-in-tournament/

# https://leetcode.com/submissions/detail/441578285/
# 01/11/2021 04:23  

class Solution:
    def numberOfMatches(self, n: int) -> int:
        count = 0
        while n > 1:
            if n % 2 == 0:
                n //= 2
                count += n
            else:
                count += (n - 1) // 2
                n = ((n - 1) // 2) + 1
        return count