# https://leetcode.com/problems/maximum-69-number/

# https://leetcode.com/submissions/detail/442271820/
# 01/12/2021 18:38  

class Solution:
    def maximum69Number (self, num: int) -> int:
        result = ""
        changed = False
        for d in str(num):
            if d == "6" and not changed:
                changed = True
                result += "9"
            else:
                result += d
        return int(result)