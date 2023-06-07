# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def getAncestors(lst:List['TreeNode'], root:'TreeNode', node: 'TreeNode'):
      
            if not root:
                return False
            lst.append(root)
            if root.val==node.val:
                return True
            if ((root.left!=None and getAncestors(lst, root.left, node)) or (root.right!=None and getAncestors(lst, root.right, node))):
                return True
            lst.pop()
            return False

        ancestors_p:List['TreeNode']=[]
        ancestors_q:List['TreeNode']=[]
        
        res=getAncestors(ancestors_p, root, p)        
        res=getAncestors(ancestors_q, root, q)
        
        for node in reversed(ancestors_p):
            if node in ancestors_q:
                return node
        return root
