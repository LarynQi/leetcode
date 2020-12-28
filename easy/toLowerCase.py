# https://leetcode.com/problems/to-lower-case/

# https://leetcode.com/submissions/detail/268871292/
# 10/10/2019 23:58  

class Solution:
    def toLowerCase(self, str: str) -> str:
        new = ''
        for letter in str:
            if ord(letter) <= ord('Z') and ord(letter) >= ord('A'):
                letter = chr(ord(letter) + 32)
            new += letter
        return new