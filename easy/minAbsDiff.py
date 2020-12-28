# https://leetcode.com/problems/minimum-absolute-difference/

# https://leetcode.com/submissions/detail/288647889/
# 12/25/2019 23:29  
# Wrong Answer

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        result = []
        while len(arr) > 1:
            copy = arr[:] 
            copy.remove(min(copy))
            diff = min(copy) - min(arr)
            if not result or diff == result[0][1] - result[0][0]:
                result += [[min(arr), min(copy)]]
            arr.remove(min(arr))
        return result