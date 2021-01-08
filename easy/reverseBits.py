# https://leetcode.com/problems/reverse-bits/

# https://leetcode.com/submissions/detail/440241610/
# 01/08/2021 02:45  

class Solution:
    def reverseBits(self, n: int) -> int:
        binary = str(bin(n))[2:]
        while len(binary) < 32:
            binary = "0" + binary
        result = 32 * [0]
        for i in range(16):
            result[i] = binary[-(i + 1)]
            result[-(i + 1)] = binary[i]
        binary = ""
        for n in result:
            binary += str(n)
        return int(binary, 2)