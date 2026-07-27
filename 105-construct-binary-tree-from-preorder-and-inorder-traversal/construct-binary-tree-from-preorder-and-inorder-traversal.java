/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    private Map<Integer, Integer> inorderIndexes = new HashMap<>();
    private int i_pre;
    private TreeNode solve(int[] preorder, int[] inorder, int start, int end) {
        if (start > end || i_pre >= preorder.length)
            return null;
        TreeNode node = new TreeNode(preorder[i_pre]);
        int i_in = inorderIndexes.get(preorder[i_pre]);
        i_pre++;
        node.left = solve(preorder, inorder, start, i_in - 1);
        node.right = solve(preorder, inorder, i_in + 1, end);
        return node;
    }
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        for (int i = 0; i < inorder.length; i++)
            inorderIndexes.put(inorder[i], i);
        i_pre = 0;
        return solve(preorder, inorder, 0, inorder.length - 1);
    }
}