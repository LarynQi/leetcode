# https://leetcode.com/problems/find-and-replace-pattern/

# https://leetcode.com/submissions/detail/291862043/
# 01/06/2020 15:46  

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def match(word):
            cache = {}
            for i in range(len(pattern)):
                if pattern[i] not in cache:
                    if word[i] in cache.values():
                        return False
                    else:
                        cache[pattern[i]] = word[i]
                else:
                    if word[i] != cache[pattern[i]]:
                        return False
            return True
        return list(filter(match, words))