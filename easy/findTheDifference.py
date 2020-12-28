# https://leetcode.com/problems/find-the-difference/

# https://leetcode.com/submissions/detail/283390512/
# 12/02/2019 22:54  

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        cache = {}
        #all letters used in s
        for letter in s:
            cache[letter] = cache.get(letter, 0) + 1
            
        #checking used letters
        for letter in t:
            if letter not in cache:
                return letter
            else:
                cache[letter] -= 1
        
        #filtering cache to find extra added letter
        for key in cache.keys():
            if cache[key] != 0:
                return key