# https://leetcode.com/problems/destination-city/

# https://leetcode.com/submissions/detail/442279236/
# 01/12/2021 18:59  

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        inputs = set()
        outputs = set()
        for p in paths:
            inputs.add(p[0])
            outputs.add(p[1])
        return next(iter(outputs - inputs))