# https://leetcode.com/problems/uncommon-words-from-two-sentences/

# https://leetcode.com/submissions/detail/440519182/
# 01/08/2021 19:25  

class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        seen_A = set()
        blacklist_A = set()
        for w in A.split():
            if w in seen_A:
                blacklist_A.add(w)
            seen_A.add(w)
        seen_B = set()
        blacklist_B = set()
        for w in B.split():
            if w in seen_B:
                seen_B.remove(w)
                blacklist_B.add(w)
            seen_B.add(w)
        # print(seen_A, seen_B)
        return list((seen_A ^ seen_B) - blacklist_A - blacklist_B)