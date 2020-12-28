# https://leetcode.com/problems/unique-number-of-occurrences/

# https://leetcode.com/submissions/detail/269049933/
# 10/11/2019 17:27  

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occur = {}
        for val in arr:
            if not occur.get(val):
                occur[val] = 1
            else:
                occur[val] += 1
        for i in arr:
            for j in arr:
                if i != j and occur[i] == occur[j]:
                    return False
        return True