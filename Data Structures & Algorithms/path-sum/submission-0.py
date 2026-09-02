# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def helper(node,targetSum):
            if not node:
                return False
            if not node.left and not node.right: 
                return targetSum == node.val
            remaining = targetSum - node.val
            return helper(node.left,remaining) or helper(node.right,remaining)
        return helper(root,targetSum)