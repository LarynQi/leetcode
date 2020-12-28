# https://leetcode.com/problems/rearrange-words-in-a-sentence/

# https://leetcode.com/submissions/detail/434037968/
# 12/24/2020 02:06  

class Solution:
    def arrangeWords(self, text: str) -> str:
        occurrences = []
        mapping = {}
        for s in text.split():
            curr = len(s)
            if curr not in mapping:
                mapping[curr] = len(occurrences)
                occurrences.append([])
            lst = occurrences[mapping[curr]]
            if lst:
                lst.append(s.lower())
            else:
                occurrences[mapping[curr]] = [s.lower()]
        output = ""
        count = 0
        for l in {k: v for k, v in sorted(mapping.items(), key=lambda p: p[0])}:
            i = mapping[l]
            if count == 0:
                for j in range(len(occurrences[i])):
                    if j == 0:
                        output += occurrences[i][0][0].upper() + occurrences[i][0][1:] + " "
                    else:
                        output += occurrences[i][j] + " "
            else:
                for s in occurrences[i]:
                    output += s + " "
            count += 1
                
        # for i in range(len(occurrences)):
        #     if i == 0:
        #         for j in range(len(occurrences[i])):
        #             if j == 0:
        #                 output += occurrences[i][0][0].upper() + occurrences[i][0][1:] + " "
        #             else:
        #                 output += ocurrences[i][j] + " "
        #     else:
        #         for s in occurrences[i]:
        #             output += s + " "
        return output[:-1]