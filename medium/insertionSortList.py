# https://leetcode.com/problems/insertion-sort-list/

# https://leetcode.com/submissions/detail/439786359/
# 01/07/2021 03:57  

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        output = None
        tail = None
        
        while head:
            next_head = head.next
            if not output:
                output = head
                output.prev = None
                tail = output
            else:
                if tail.val < head.val:
                    tail.next = head
                    head.prev = tail
                    tail = head
                else:
                    ptr = tail
                    while ptr and ptr.val >= head.val:
                        ptr = ptr.prev
                    if not ptr:
                        output.prev = head
                        save = output
                        output = head
                        output.prev = None
                        output.next = save
                        tail.next = next_head
                    else:
                        ptr.next.prev = head
                        head.prev = ptr
                        head.next = ptr.next
                        ptr.next = head
                        tail.next = next_head
                        # ptr.next, head.next, ptr.next.prev, head.prev = head, ptr.next, head, ptr

            head = next_head
        return output
        ### selection sort ###
        # if not head:
        #     return None
        # output = None
        # length = 0
        # i = 0
        # # seen = set()
        # occurrences = {float("inf"): 1}
        # last = None
        # while not length or i < length:
        #     ptr = head
        #     smallest = float("inf")
        #     while ptr:
        #         if not output:
        #             length += 1
        #             occurrences[ptr.val] = occurrences.get(ptr.val, 0) + 1
        #         if occurrences[ptr.val] > 0:
        #             smallest = min(ptr.val, smallest)
        #         ptr = ptr.next
        #     occurrences[smallest] -= 1
        #     if not last:
        #         last = ListNode(smallest)
        #         output = last
        #     else:
        #         last.next = ListNode(smallest)
        #         last = last.next
        #     # seen.add(smallest)
        #     i += 1
        # return output