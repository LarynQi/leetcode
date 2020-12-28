# https://leetcode.com/problems/valid-anagram/

# https://leetcode.com/submissions/detail/283387253/
# 12/02/2019 22:39

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cache = {}
        
        #adding all used letters in s
        for letter in s:
            cache[letter] = cache.get(letter, 0) + 1
        
        #is t an anagram?
        for letter in t:
            if letter not in cache:
                return False
            else:
                cache[letter] -= 1
                
        #making sure all letters used correct number of times
        for n in cache.values():
            if n != 0:
                return False
        return True