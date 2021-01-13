# https://leetcode.com/problems/perfect-number/

# https://leetcode.com/submissions/detail/442009380/
# 01/12/2021 03:21  

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        
        ### Solution ###
        
        total = 0
        for n in range(1, int(num ** 0.5) + 1):
            if num % n == 0 and n != num:
                total += n + num // n
        return total - num == num
        
        ### Naive ###
        # divisors = set()
        # for n in range(1, num // 2 + 1):
        #     if num % n == 0:
        #         divisors.add(n)
        # return sum(divisors) == num