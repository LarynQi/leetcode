# https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/

# https://leetcode.com/submissions/detail/441575520/
# 01/11/2021 04:09  

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        if not word1 and not word2:
            return True
        if not word1 or not word2:
            return False
        if word1[0][0] != word2[0][0]:
            return False
        # word1 = word1[:]
        # word2 = word2[:]
        if len(word1[0]) == 1:
            if len(word2[0]) == 1:
                return self.arrayStringsAreEqual(word1[1:], word2[1:])
            else:
                word2[0] = word2[0][1:]
                return self.arrayStringsAreEqual(word1[1:], word2)
        elif len(word2[0]) == 1:
            word1[0] = word1[0][1:]
            return self.arrayStringsAreEqual(word1, word2[1:])
        word1[0] = word1[0][1:]
        word2[0] = word2[0][1:]
        return self.arrayStringsAreEqual(word1, word2)