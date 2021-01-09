# https://leetcode.com/problems/find-common-characters/

# https://leetcode.com/submissions/detail/440522840/
# 01/08/2021 19:38  

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        occurrences = [{} for _ in range(len(A))]
        for i in range(len(A)):
            s = A[i]
            for c in s:
                occurrences[i][c] = occurrences[i].get(c, 0) + 1
        result = []
        seen = set()
        for o in occurrences:
            for c in o:
                if all([c in occur for occur in occurrences]) and c not in seen:
                    seen.add(c)
                    count = min([occur[c] for occur in occurrences])
                    while count > 0:
                        result.append(c)
                        count -= 1
        return result