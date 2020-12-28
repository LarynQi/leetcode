# https://leetcode.com/problems/defanging-an-ip-address/

# https://leetcode.com/submissions/detail/268724596/
# 10/10/2019 13:55  

class Solution:
    def defangIPaddr(self, address: str) -> str:
        defang = ''
        for i in range(len(address)):
            if address[i] == '.':
                defang += '[.]'
            else:
                defang += address[i]
        return defang