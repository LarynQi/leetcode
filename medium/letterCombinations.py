# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

# https://leetcode.com/submissions/detail/447508607/
# 01/24/2021 21:56  

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # lookup hashtable mapping digits to letters
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        def helper(digits, sofar):
            if not digits:
                return sofar
            curr = digits[0]
            ret = []
            if sofar:
                for s in sofar:
                    for c in mapping[curr]:
                        ret.append(s + c)
            else:
                for c in mapping[curr]:
                    ret.append(c)
            return helper(digits[1:], ret)
        return helper(digits, [])