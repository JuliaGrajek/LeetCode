# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.result : List[int] = []
        self.levels = defaultdict(int)

        def height(node)->int:
            if node is None:
                return 0
            else:
                lheight=height(node.left)
                rheight=height(node.right)
                if lheight>rheight:
                    return lheight+1
                else:
                    return rheight+1

        def returnCurrentLevel(root,level)->List[TreeNode]:       
            if root is None:
                return
            if level==1:
                self.levels[1]=[root]
            elif level>1:
                self.levels[level]=[]
                for node in self.levels[level-1]:
                        if node.left:
                            self.levels[level].append(node.left)
                        if node.right:
                            self.levels[level].append(node.right)
                        
        h = height(root)
        for level in range(h):
            returnCurrentLevel(root, level+1)
            
            self.result.append(self.levels[level+1][-1].val)
        return self.result
Console
