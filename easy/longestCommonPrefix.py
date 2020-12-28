# https://leetcode.com/problems/longest-common-prefix/submissions/

# https://leetcode.com/submissions/detail/268722722/
# 10/10/2019 13:48  
# Wrong Answer

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = ''
        letter = 0
        other_word = 1
        other_letter = 0
        if not strs:
            return pre
        elif len(strs) == 1:
            return strs[0]
        
        first = strs[0]
        check = True
        
        for i in strs:
            if i != first:
                check = False
        if check:
            return first
        
        shortest = strs[0]
        for k in strs:
            if len(k) < len(shortest):
                shortest = k
        while letter < len(strs[0]):
            while other_word < len(strs):
                while other_letter < len(strs[other_word]):
                    if strs[0][letter] == strs[other_word][other_letter]:
                        if strs[other_word] == shortest and other_letter == len(strs[other_word]) - 1:
                            pre += strs[0][letter]
                            return pre
                        elif other_word == len(strs) - 1:
                            pre += strs[0][letter]
                            letter += 1
                            other_word = 1
                            other_letter = letter
                        else:
                            other_word += 1
                            other_letter = letter
                    else:
                        return pre
        return pre