# https://leetcode.com/problems/word-pattern/

# https://leetcode.com/submissions/detail/291988286/
# 01/06/2020 23:34  

class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        cache = {}
        words = []
        build = ""
        for i in range(len(str)):
            if str[i] != " ":
                build += str[i]
            if i + 1 == len(str) or str[i + 1] == " ":
                words += [build]
                build = ""
        if len(words) != len(pattern):
            return False
        for i in range(len(words)):
            if pattern[i] in cache:
                if words[i] != cache[pattern[i]]:
                    return False
            cache[pattern[i]] = words[i]
            dupe = list(dict(cache).values())
            if words[i] in dupe:
                dupe.remove(words[i])
                if words[i] in dupe:
                    return False         
        return True