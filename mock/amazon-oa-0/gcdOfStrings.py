# https://leetcode.com/problems/greatest-common-divisor-of-strings/

# https://leetcode.com/interview/reports/SW50ZXJ2aWV3U2Vzc2lvbk5vZGU6MTQ0NjM4OA==

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Brute Force
        def divides(s, t):
            if t == "":
                return True
            save = t
            while len(t) <= len(s):
                if t == s:
                    return True
                t += save
            return False
        if len(str1) >= len(str2):
            dividend = str1
            divisor = str2
            save = divisor
        else:
            dividend = str2
            divisor = str1
            save = divisor
        while not divides(dividend, divisor) or not divides(save, divisor):
            divisor = divisor[:-1]   
        return divisor
    
        # factor = ""
        # while not divides(str1, factor) or not divides(str2, factor):
            
#         def helper(s1, s2, factor):
#             if not s1 or not s2:
#                 return factor
#             curr = factor + s1[0]
#             if divides(s1, curr) and divides(s2, curr):
#                 return helper(s1, s2, curr)    
            
            
#         return helper(str1, str2, "")