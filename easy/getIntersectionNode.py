# https://leetcode.com/problems/intersection-of-two-linked-lists/

# https://leetcode.com/submissions/detail/291900222/
# 01/06/2020 18:25

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        cacheA = {}
        cacheB = {}
        while headA or headB:
            if headA is headB:
                return headA
            if headA in cacheB:
                return headA
            if headB in cacheA: 
                return headB
            cacheA[headA] = 1
            cacheB[headB] = 1
            if headA:
                headA = headA.next
            if headB:
                headB = headB.next