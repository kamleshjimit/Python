
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
                       
        def helper(root, min, max) -> bool:
            if root == None:
                return True

            if (min != None and root.val <= min) or (max!=None and root.val >= max):
                return False
        
            return helper(root.left, min, root.val) and helper(root.right, root.val, max)
        
        return helper(root, None, None)