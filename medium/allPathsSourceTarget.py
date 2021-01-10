# https://leetcode.com/problems/all-paths-from-source-to-target/

# https://leetcode.com/submissions/detail/441018316/         
# 01/09/2021 21:58  

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def helper(graph, curr, sofar):
            if curr == len(graph) - 1:
                return [sofar + [curr]]
            else:
                ret = []
                for n in graph[curr]:
                    ret.extend(helper(graph, n, sofar + [curr]))
                return ret
        return helper(graph, 0, [])

# https://leetcode.com/submissions/detail/441017679/
# 01/09/2021 21:56  

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def helper(graph, curr, seen, sofar):
            if curr == len(graph) - 1:
                ret = sofar + [curr]
                seen[sofar[0]] = sofar
                return [ret]
            else:
                ret = []
                for n in graph[curr]:
                    if n in seen:
                        ret.append(sofar + seen[n])
                    else:
                        ret.extend(helper(graph, n, seen, sofar + [curr]))
                return ret
        return helper(graph, 0, {}, [])
