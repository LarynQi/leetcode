# https://leetcode.com/problems/find-eventual-safe-states/

# https://leetcode.com/submissions/detail/433917913/
# 12/23/2020 18:34
# Time Limit Exceeded

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        def cycles(g, i, seen, terminates):
            # if i in terminates:
            #     print('here', i)
            if not g[i] or i in terminates:
                return False
            # if not g[i]:
            elif i in seen:
                return True
            # seen.add(i)
            new_seen = set(seen)
            new_seen.add(i)
            # return any([cycles(g, n, new_seen, terminates) for n in g[i]])
            # generator = (cycles(g, n, new_seen, terminates) for n in g[i])
            # for el in generator:
            #     if el:
            #         return True
            # return False
            for n in g[i]:
                if cycles(g, n, new_seen, terminates):
                    return True
            return False
        result = []
        terminates = set()
        for n in range(len(graph)):
            if not cycles(graph, n, set(), terminates):
                result.append(n)
                terminates.add(n)
        return result