# https://leetcode.com/problems/convert-a-number-to-hexadecimal/

# https://leetcode.com/submissions/detail/434231688/
# 12/24/2020 16:24  

class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        conversion = {
            10: "a",
            11: "b",
            12: "c",
            13: "d",
            14: "e",
            15: "f"
        }
        def convert(num):
            result = ""
            count = 0
            while abs(num) > 0 and count < 8:
                curr = (num & 1) + (num & 2) + (num & 4) + (num & 8)
                if curr >= 10:
                    curr = conversion[curr]
                result = str(curr) + result
                num >>= 4
                count += 1
            return result
        if num > 0:
            return convert(num)
        else:
            return convert(num)