# https://leetcode.com/problems/merge-in-between-linked-lists/

# https://leetcode.com/submissions/detail/442331424/
# 01/12/2021 21:19  

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        
        link_a = link_b = list1
        while b > 0:
            if a > 1:
                link_a = link_a.next
                a -= 1
            link_b = link_b.next
            b -= 1
                    
        link_a.next = list2
        ptr = list2
        while ptr.next:
            ptr = ptr.next
        ptr.next = link_b.next
        return list1
        
        
        # link_a = link_b = list1
        # while True:
        #     if link_a != a:
        #         link_a = link_a.next
        #     if link_b != b.next:
        #         link_b = link_b.next
        #     else:
        #         break
        # link_a.next = list2
        # ptr = list2
        # while ptr.next:
        #     ptr = ptr.next
        # ptr.next = link_b
        # return list1