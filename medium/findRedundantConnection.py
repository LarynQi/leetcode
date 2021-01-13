# https://leetcode.com/problems/redundant-connection/

# https://leetcode.com/submissions/detail/442382142/
# 01/12/2021 23:37  
# Failed

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # class Node():
        #     def __init__(self, val):
        #         self.val = val
        #         self.prev = set()
        #         self.next = set()
        #     def __str__(self):
        #         return f"Val: {self.val}, Prev: {self.prev}, Next: {self.next}"
        # nodes = [Node(i) for i in range(1, len(edges) + 1)]
        # for e in edges:
        #     frm = e[0] - 1
        #     to = e[1] - 1
        #     nodes[frm].next.add(to)
        #     nodes[to].prev.add(frm)
        # for i in range(len(edges) - 1, -1, -1):
        #     e = edges[i]
        #     if len(nodes[e[1] - 1].prev) > 1:
        #         return e
        
        # inputs = set()
        # outputs = set()
        # redundant = []
        # for e in edges:
        #     inputs.add(e[0])
        #     outputs.add(e[1])
        # for e in edges:
        #     if e[0] in outputs and e[1] in outputs:
        #         redundant.append(e)
        # return redundant[-1]
        
        class Node:
            def __init__(self, val):
                self.val = val
                self.head = None
                self.children = set()
            def __str__(self):
                return str(self.val)
        nodes = [Node(i) for i in range(1, len(edges) + 1)]      
        outputs = set()
        inputs = set()
        count = 0
        for e in edges:
            count += 1
            frm = nodes[e[0] - 1]
            to = nodes[e[1] - 1]
            if frm.head:
                ptr = frm.head
            else:
                ptr = frm
            # ptr = frm
            # while ptr.head:
            #     ptr = ptr.head
            print(e, to.head, ptr)
            # if to.head and to.head.val == frm.val and e[1] in outputs:
            if e[1] in outputs | inputs and (to.head is ptr or (not frm.head and not to.head and not frm)) or count == len(edges):
                return e
            to.head = ptr
            frm.children.add(to.val)
            outputs.add(e[1])
            inputs.add(e[0])
        # for n in nodes:
        #     if n.head:
        #         head = n.head
        #         break
        # print(head.val, head.children)
        # for i in range(len(edges) - 1, -1, -1):
        #     e = edges[i]
        #     if e[1] in head.children:
        #         return e
            