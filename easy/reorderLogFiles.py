# https://leetcode.com/problems/reorder-data-in-log-files/

# https://leetcode.com/submissions/detail/436228091/
# 12/29/2020 18:36  
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digit_logs = []
        
        for l in logs:
            curr = l.split()
            if curr[1].isalpha():
                letter_logs.append((curr[0], l[len(curr[0]) + 1:], l))
            else:
                digit_logs.append(l)
        def letter_comparator(l1, l2):
            if l1[1] != l2[1]:
                return l1[1] < l2[1]
            else:
                return l1[0] < l2[0]
            
        def mergesort(lst):
            if len(lst) == 1:
                return lst
            left = mergesort(lst[:len(lst) // 2])
            right = mergesort(lst[len(lst) // 2:])
            return merge(left, right)
        
        def merge(l1, l2):
            i1 = i2 = 0
            result = []
            while i1 < len(l1) and i2 < len(l2):
                if letter_comparator(l1[i1], l2[i2]):
                    result.append(l1[i1])
                    i1 += 1
                else:
                    result.append(l2[i2])
                    i2 += 1
            if i1 < len(l1):
                result.extend(l1[i1:])
            elif i2 < len(l2):
                result.extend(l2[i2:])
            return result
        
        letter_logs = mergesort(letter_logs)
        letter_logs = [l[2] for l in letter_logs]
        # for l in logs:
        #     if l[:3] == "let":
        #         letter_logs.append(l)
        #     elif l[:3] == "dig":
        #         digit_logs.append(l)
        #     else:
        #         print("Unexpected log type.")
        #         return []
        # letter_logs.sort(key=lambda s: s[5:])
        # def letter_comparator(l1, l2):
        #     comp1 = l1[5:]
        #     comp2 = l2[5:]
        #     if comp1 != comp2:
        #         return 
        return letter_logs + digit_logs
        # letter_logs.extend(digit_logs)
        # return letter_logs