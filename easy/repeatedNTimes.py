# https://leetcode.com/problems/n-repeated-element-in-size-2n-array/

# https://leetcode.com/submissions/detail/269138210/
# 10/12/2019 01:24  

class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        dict = {}
        for i in A:
            if not dict.get(i):
                dict[i] = 1
            else:
                return i