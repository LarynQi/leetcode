# https://leetcode.com/problems/squares-of-a-sorted-array/

# https://leetcode.com/submissions/detail/269139946/
# 10/12/2019 01:36  
# Time Limit Exceeded

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        A = [x ** 2 for x in A]
        count = 0
        while count < len(A):
            i = 1
            while i < len(A):
                if A[i - 1] > A[i]:
                    A[i], A[i - 1] = A[i - 1], A[i]
                i += 1
            count += 1
        return A