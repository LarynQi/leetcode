# https://leetcode.com/problems/di-string-match/

# https://leetcode.com/submissions/detail/269390267/
# 10/12/2019 21:25  
# Wrong Answer

class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        new = [len(S)]
        for i in range(1, len(S) + 1):
            if S[i - 1] == 'I':
                new += [1 + new[i - 1]]
            else:
                new += [new[i - 1] - 1]
        return new