# https://leetcode.com/problems/flipping-an-image/

# https://leetcode.com/submissions/detail/442273661/
# 01/12/2021 18:43  

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for i in range(len(A)):
            r = A[i]
            left = 0
            right = len(r) - 1
            while left < right:
                temp = r[left]
                r[left] = int(not r[right])
                r[right] = int(not temp)
                left += 1
                right -= 1
            if left == right:
                r[left] = int(not r[left])
        return A