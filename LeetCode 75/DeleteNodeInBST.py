# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        def findSuccessor(root:Optional[TreeNode]):
            curr = root
            while curr.left is not None:
                curr=curr.left
            return curr

        def deleteNodeBST(root:Optional[TreeNode], key:int) -> Optional[TreeNode]:
            if root is None:
                return None
            if root.val>key:
                root.left = deleteNodeBST(root.left, key)
            elif root.val<key:
                root.right = deleteNodeBST(root.right, key)
            else:
                if not root.left and not root.right:
                    return None
                elif not root.left:
                    return root.right
                elif not root.right:
                    return root.left
                else:
                    successor=findSuccessor(root.right)
                    root.val=successor.val
                    root.right=deleteNodeBST(root.right, successor.val)
            return root

        res =deleteNodeBST(root, key)
        return res
