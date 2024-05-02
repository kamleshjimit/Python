from typing import List, Optional
from Python.compression.huffman import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = {}
        
        def helper(root: Optional[TreeNode], level:int):     
            if root == None:
                return
        
            if level not in result:
                result[level] = []
            result[level].append(root.val)
            level += 1
            helper(root.left, level)
            helper(root.right, level)
        
        
        helper(root, 0)
        return result.values()

