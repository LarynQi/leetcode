# https://leetcode.com/problems/happy-number/

# https://leetcode.com/submissions/detail/440199190/
# 01/08/2021 00:10  

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while True:
            temp = n
            total = 0
            while temp > 0:
                total += (temp % 10) ** 2
                temp //= 10
            n = total
            if n == 1:
                return True
            if n in seen:
                return False
            seen.add(n)
