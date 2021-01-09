# https://leetcode.com/problems/monotonic-array/

# https://leetcode.com/submissions/detail/440516697/
# 01/08/2021 19:16  

class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        prev = None
        increasing = None
        for n in A:
            if prev is None:
                prev = n
            elif n != prev:
                if increasing is None:
                    increasing = True if n > prev else False
                elif increasing:
                    if n < prev:
                        return False
                else:
                    if n > prev:
                        return False
                prev = n
        return True
        