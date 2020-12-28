# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

# https://leetcode.com/submissions/detail/288177841/
# 12/23/2019 22:53  

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        temp = n
        while temp >= 10:
            if temp % 10 == 0:
                product = 0
                break
            product *= temp % 10
            temp //= 10
        product *= temp
        total = n % 10
        while n >= 10:
            n //= 10
            total += n % 10
        return product - total