# https://leetcode.com/problems/shortest-distance-to-a-character/

# https://leetcode.com/submissions/detail/288752520/
# 12/26/2019 11:03  

class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        indices = []
        for i in range(len(S)):
            if S[i] == C:
                indices += [i]
        result = []
        for i in range(len(S)):
            result += [min([abs(index - i) for index in indices])]
        return result