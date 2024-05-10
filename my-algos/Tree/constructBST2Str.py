# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def preorder(root):
            if not root:
                return ""  # Empty string for missing nodes

            # Base case: Leaf node (no children)
            if not root.left and not root.right:
                return str(root.val)

            # Case with left child only
            if not root.right:
                return str(root.val) + "(" + preorder(root.left) + ")"

            # Case with both children
            return str(root.val) + "(" + preorder(root.left) + ")" + "(" + preorder(root.right) + ")"

        # Perform preorder traversal and return the string
        result = preorder(root)
        return result

