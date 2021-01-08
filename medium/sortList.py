# https://leetcode.com/problems/sort-list/

# https://leetcode.com/submissions/detail/439962891/
# 01/07/2021 13:08  
# Infinite Recursion

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        #### Merge sort ###
        ptr = head
        prev = None
        while ptr:
            ptr.prev = prev
            prev = ptr
            if not ptr.next:
                tail = ptr
            ptr = ptr.next
            
        def mergesort(head, tail):
            if not head.next or head is tail:
                return
            slow = head
            fast = head
            while fast and fast.next:
                slow = slow.next
                if fast is tail or fast.next is tail:
                    break
                fast = fast.next.next
            mergesort(head, slow)
            mergesort(slow, tail)
            merge(head, slow)
            
        def merge(head1, head2):
            save2 = head2
            next_prev = head1.prev
            while head1 and head2:
                if head1.val > head2.val:
                    head1.prev.next = head2
                    head2.prev = head1.prev.next
                    next_prev = head2
                    head2 = head2.next
                else:
                    head1.prev = next_prev
                    next_prev = head1
                    head1 = head1.next
            if not head1:
                next_prev.next = head2
                head2.prev = next_prev
            if not head2:
                head1.prev = next_prev
                while head1.next is not head2:
                    head1 = head1.next
                head1.next = next_prev
        mergesort(head, tail)
                    