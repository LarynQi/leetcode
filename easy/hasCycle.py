# https://leetcode.com/problems/linked-list-cycle/

# https://leetcode.com/submissions/detail/439627811/
# 01/06/2021 19:41  

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        ### Solution: 2 pointers
        
        slow = head
        if not slow:
            return False
        fast = head.next
        while fast is not None:
            if slow is fast:
                return True
            slow = slow.next
            if fast.next is None:
                break
            fast = fast.next.next
            
        return False
        
        ### Extra flag ###
        # while head is not None:
        #     try:
        #         curr = head.flag
        #         return True
        #     except:
        #         head.flag = True
        #         head = head.next
        # return False
    
        ### O(n) memory ###
        # seen = set()
        # while head is not None:
        #     if head in seen:
        #         return True
        #     else:
        #         seen.add(head)
        #         head = head.next
        # return False