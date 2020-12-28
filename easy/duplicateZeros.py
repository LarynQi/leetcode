# https://leetcode.com/problems/duplicate-zeros/

# https://leetcode.com/submissions/detail/275277518/
# 11/02/2019 02:36  

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        copy = arr[:]
        count = 0
        for i in range(len(copy)):
            if copy[i] == 0:
                arr.insert(i + count, 0)
                count += 1
        while (len(arr)) > len(copy):
            arr.pop()
            