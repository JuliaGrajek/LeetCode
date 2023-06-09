# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from copy import copy
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        def findNode(root: Optional[TreeNode], val:int)->Optional[TreeNode]:
            if root:
                if root.val<val:
                    return findNode(root.right,val)
                elif root.val> val:
                    return findNode(root.left,val)
                else:
                    return root
        
        res: Optional[TreeNode]
        res=findNode(root, val)
        return res
