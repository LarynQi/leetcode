// https://leetcode.com/problems/n-ary-tree-postorder-traversal/

// https://leetcode.com/submissions/detail/434885003/
// 12/26/2020 13:40

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
    public List<Integer> postorder(Node root) {
        ArrayList result = new ArrayList();
        Stack s = new Stack();
        s.push(root);

        Node curr;
        while (!s.isEmpty()) {
            curr = (Node) s.pop();
            if (curr != null) {
                result.add(curr.val);
                // for (int i = curr.children.size() - 1; i >= 0; i -= 1) {
                //     s.push(curr.children.get(i));
                // }
                for (Node n : curr.children) {
                    s.push(n);
                }
            }

        }
        Collections.reverse(result);
        return result;
        // Node curr = root;
        // while (curr != null) {
        //     s.push(curr);
        //     curr = curr.children[0];
        // }
        // while (!s.isEmpty()) {
        //     curr = s.pop();
        //     result.add(curr.val);
        //     s.push(curr.children[1])
        // }
        // while (!s.isEmpty()) {
        //     curr = s.pop();
        //     for (int i = curr.children.length - 1; i >= 0; i -= 1) {
        //         s.push(curr.children[i]);
        //     }
        //     result.add(curr)
        // }
        
        // // Recursive
        // ArrayList result = new ArrayList();
        // if (root == null) {
        //     return result;
        // }
        // if (root.children != null) {
        //     for (Node n : root.children) {
        //         result.addAll(postorder(n));
        //     }
        //     result.add(root.val);
        //     return result;
        // } else {
        //     result.add(root.val);
        //     return result;
        // }
    }
}