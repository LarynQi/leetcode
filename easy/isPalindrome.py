# https://leetcode.com/problems/palindrome-number/

# https://leetcode.com/submissions/detail/268605664/
# 10/10/2019 02:28

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 10 and x >= 0:
            return True
        if x < 0:
            return False
        new = 0
        k = x
        while k > 0:
            new = new * 10 + k % 10
            k //= 10
        return new == x