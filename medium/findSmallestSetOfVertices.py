# https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/

# https://leetcode.com/submissions/detail/442342081/
# 01/12/2021 21:47  

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        all_nodes = set([i for i in range(n)])
        outputs = set()
        for e in edges:
            outputs.add(e[1])
        return list(all_nodes - outputs)
        