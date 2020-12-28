# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

# https://leetcode.com/submissions/detail/288176483/
# 12/23/2019 22:46  

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for n in nums:
            digits = 1
            while n >= 10:
                digits += 1
                n //= 10
            if digits % 2 == 0:
                count += 1
        return count