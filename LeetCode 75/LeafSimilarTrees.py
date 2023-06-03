# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def returnLeaves(root: Optional[TreeNode]) ->List[Optional[TreeNode]]:
            leaves=[]
            node:Optional[TreeNode]=root
            if not node.left and not node.right:
                leaves.append(node.val)
                return leaves
            elif not node.left:
                return returnLeaves(node.right)
            elif not node.right:
                return returnLeaves(node.left)
            else:
                return returnLeaves(node.left)+returnLeaves(node.right)
            
        leaves1 = returnLeaves(root1)
        leaves2 = returnLeaves(root2)

        return (leaves1==leaves2)
