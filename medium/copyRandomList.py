# https://leetcode.com/problems/copy-list-with-random-pointer/

# https://leetcode.com/submissions/detail/447522914/
# 01/24/2021 22:34  

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        # loop until ptr is None
        result = None
        randoms = []
        random_indices = []
        nodes = []
        save = head
        ptr = None
        while head is not None:
            if result is None:
                result = Node(head.val)
                nodes.append(result)
                randoms.append(head.random)
                random_indices.append(0)
                ptr = result
            else:
                new = Node(head.val)
                result.next = new
                nodes.append(new)
                result = result.next
                randoms.append(head.random)
                random_indices.append(0)
            head = head.next
            
        count = 0
        head = save
        while save is not None:
            for i in range(len(randoms)):
                n = randoms[i]
                if n is save:
                    random_indices[i] = count
                if n is None:
                    random_indices[i] = -1
            save = save.next
            count += 1
        for i in range(len(random_indices)):
            target = random_indices[i]
            if target != -1:
                nodes[i].random = nodes[target]
            else:
                nodes[i].random = None
        return ptr