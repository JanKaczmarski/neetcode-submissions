# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if self.same(root, subRoot):
            return True

        if root:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
        return False

    def same(self, a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
        if not a and not b:
            return True

        if not a or not b:
            return False

        return a.val == b.val and self.same(a.left, b.left) and self.same(a.right, b.right)
        
        