"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:            
        
        def recursive_preorder_traversal(node: 'Node')->'Node':
            k=0
            res: List[int]=[]   
            if node:
                k+=1
                res.append(node.val)
                for i in range(len(node.children)):
                    res+=recursive_preorder_traversal(node.children[i])
            return res
        
        return recursive_preorder_traversal(root)
