# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/

# https://leetcode.com/submissions/detail/288186966/
# 12/23/2019 23:39  

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        def reverse(link):
            prev = None
            while link is not None:
                curr = link
                link = link.next
                curr.next, prev = prev, curr
            return curr
        head = reverse(head)
        n = 0
        result = 0
        while head is not None:
            if head.val == 1:
                result += pow(2, n)
            n += 1
            head = head.next
        return result