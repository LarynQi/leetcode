# https://leetcode.com/problems/top-k-frequent-elements/

# https://leetcode.com/submissions/detail/440233196/
# 01/08/2021 02:07  

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurrences = {}
        top_k = []
        min_k = None
        seen = set()
        for n in nums:
            if n not in occurrences:
                occurrences[n] = [0, None]
            occurrences[n][0] += 1
            if n in seen:
                top_k[occurrences[n][1]][1] += 1
                if min_k[1] == occurrences[n][1]:
                    min_k = occurrences[n]
                    for i in range(len(top_k)):
                        curr = top_k[i]
                        if curr[1] < min_k[0]:
                            min_k = [curr[1], i]
            else:
                if len(top_k) == k:
                    if occurrences[n][0] > min_k[0]:
                        seen.remove(top_k[min_k[1]][0])
                        top_k[min_k[1]] = [n, occurrences[n][0]]
                        occurrences[n][1] = min_k[1]
                        min_k = occurrences[n]
                        for i in range(len(top_k)):
                            curr = top_k[i]
                            if curr[1] < min_k[0]:
                                min_k = [curr[1], i]
                        seen.add(n)
                else:
                    top_k.append([n, occurrences[n][0]])
                    occurrences[n][1] = len(top_k) - 1
                    if min_k:
                        if occurrences[n][0] < min_k[0]:
                            min_k = occurrences[n]
                    else:
                        min_k = occurrences[n]
                    seen.add(n)
            # print(top_k, min_k, seen)
                    
        return [p[0] for p in top_k]