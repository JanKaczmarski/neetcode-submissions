# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # recursion, write the:
        # <left_child_traversal>, <current_node>, <right_child_traversal>
        # if child == None, then don't write it
        def rek(n: Optional[TreeNode], arr: List[int]):
            if not n:
                return

            if n.left:
                rek(n.left, arr)
            
            arr.append(n.val)

            if n.right:
                rek(n.right, arr)

        res = []
        rek(root, res)

        return res
            
