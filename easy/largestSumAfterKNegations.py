# https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/

# https://leetcode.com/submissions/detail/440526880/
# 01/08/2021 19:52  

class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        A.sort()
        i = 0
        flag = False
        while K > 0:
            n = A[i]
            if n < 0:
                K -= 1
                A[i] *= -1
            if n == 0:
                flag = True
                break
            if n > 0:
                last_neg = i - 1
                break
            # if n > 0 and first and K > 1:
            #     first = False
            #     i = len(A) - 1
            #     n = A[i]
            #     K -= 1
            #     A[i] *= -1
            i += 1
        if not flag:
            j = len(A) - 1
            while K > 0:
                if K == 1:
                    if abs(A[i]) < abs(A[last_neg]):
                        A[i] *= -1
                    else:
                        A[last_neg] *= -1
                    break
                n = A[j]
                K -= 2
        return sum(A)