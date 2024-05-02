# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.depth = 0
        def helper(root, height):
            if not root:
                return
            height += 1
            self.depth = max(self.depth, height)
            helper(root.left, height)
            helper(root.right, height)
        
        helper(root, 0)
        return self.depth