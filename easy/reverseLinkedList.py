# https://leetcode.com/problems/reverse-linked-list/

# https://leetcode.com/submissions/detail/284225859/
# 12/06/2019 17:03

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        reverse = None
        while head is not None:
            temp = reverse
            reverse = ListNode(head.val)
            reverse.next = temp
            head = head.next
        return reverse
            
        # entire = None
        # def helper(head):
        #     nonlocal entire
        #     if head is None:
        #         return
        #     if head.next is None:
        #         entire = ListNode(head.val)
        #         return entire
        #     temp = helper(head.next)
        #     temp.next = ListNode(head.val)
        #     return temp.next
        # helper(head)
        # return entire