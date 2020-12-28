# https://leetcode.com/problems/largest-perimeter-triangle/

# https://leetcode.com/submissions/detail/269711173/
# 10/13/2019 21:42  
# Time Limit Exceeded

class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        sorted = False
        last = len(A) - 1
        while not sorted:
            sorted = True
            for i in range(last):
                if A[i] > A[i + 1]:
                    A[i], A[i + 1] = A[i + 1], A[i]
                    sorted = False
            last -= 1
        i = len(A) - 1
        while i >= 2:
            two_sides = A[i - 1] + A[i - 2]
            if two_sides > A[i]:
                return two_sides + A[i]
            i -= 1
        return 0