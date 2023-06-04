# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res:int = 0
        curr_max:int=-inf
        def check_recursively_nodes(node:TreeNode, curr_max:int, )->int:
            if not node:
                return 0
            if node.val>=curr_max:
                curr_max=node.val
                res=1
            else:
                res=0              
            return res+check_recursively_nodes(node.left, curr_max)+check_recursively_nodes(node.right, curr_max)
           

        return check_recursively_nodes(root, curr_max)
