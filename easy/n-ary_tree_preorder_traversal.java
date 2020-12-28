// https://leetcode.com/problems/n-ary-tree-preorder-traversal/

// https://leetcode.com/submissions/detail/434348187/
// 12/25/2020 00:52

//
/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, List<Node> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
    public List<Integer> preorder(Node root) {
        ArrayList result = new ArrayList<Integer>();
        LinkedList q = new LinkedList<Node>();
        q.add(root);
        Node curr;
        while (!q.isEmpty()) {
            curr = (Node) q.poll();
            if (curr != null) {
                result.add(curr.val);
                Collections.reverse(curr.children);
                for (Node n : curr.children) {
                    q.addFirst(n);
                }
            }
        }
        // PriorityQueue q = new PriorityQueue<Node>();
        // q.add(root);
        // Node curr;
        // while (!q.isEmpty()) {
        //     curr = (Node) q.poll();
        //     if (curr != null) {
        //         result.add(curr.val);
        //         for (Node n : curr.children) {
        //             q.add(n);
        //         } 
        //     }
        // }
        return result;
        
        /*
        *** Recursive ***
        ArrayList arr = new ArrayList();
        if (root != null) {
            arr.add(root.val);
            for (Node n : root.children) {
                arr.addAll(preorder(n));
            }
        }
        return arr;
        */
    }
}
