# https://leetcode.com/problems/group-anagrams/

# https://leetcode.com/submissions/detail/291201136/
# 01/04/2020 14:07

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # if not strs:
        #     return []
        # if len(strs) == 1:
        #     return [[strs[0]]]
        # anagrams = [[strs[0]]]
        # cache = {}
        # copy = strs[1:]
        # for letter in strs[0]:
        #     cache[letter] = 1 + cache.get(letter, 0)
        # for word in strs[1:]:
        #     if len(word) == len(strs[0]):
        #         cache2 = dict(cache)
        #         for letter in word:
        #             cache2[letter] = cache2.get(letter, 0) - 1
        #         if not any(cache2.values()):
        #             anagrams[0] += [word]
        #             copy.remove(word)
        # return anagrams + self.groupAnagrams(copy)
        def convert(w):
            alphabet = [0] * 26
            for letter in w:
                index = ord(letter) - ord('a')
                alphabet[index] += 1
            return tuple(alphabet)
        groupings = {}
        for word in strs:
            code = convert(word)
            if code in groupings.keys():
                groupings[code] += [word]
            else:
                groupings[code] = [word]
        return groupings.values()