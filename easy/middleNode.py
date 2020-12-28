# https://leetcode.com/problems/middle-of-the-linked-list/

# https://leetcode.com/submissions/detail/284981280/
# 12/09/2019 23:40  

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        length = 1
        while head is not None:
            counter = length
            pointer = head
            while counter > 0:
                if pointer is None or pointer.next is None:
                    return head
                pointer = pointer.next
                counter -= 1
            length += 1
            head = head.next