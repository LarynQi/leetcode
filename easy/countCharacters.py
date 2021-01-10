# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/

# https://leetcode.com/submissions/detail/440622499/
# 01/09/2021 01:14  

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        counts = []
        for w in words:
            count = 0
            curr = {}
            for c in w:
                curr[c] = curr.get(c, 0) + 1
                count += 1
            counts.append((curr, count))
        available = {}
        for c in chars:
            available[c] = available.get(c, 0) + 1
        total = 0
        for d, length in counts:
            failed = False
            for c in d:
                if c not in available or d[c] > available[c]:
                    failed = True
                    break
            if not failed:
                total += length
        return total
            