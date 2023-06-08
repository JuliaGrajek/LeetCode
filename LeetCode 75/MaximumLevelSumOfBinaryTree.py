# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
      
        max_sum:int=-inf
        res:int=-inf
        lvl:int=0
        queue = deque([root])
        while len(queue)>0:
            lvl+=1
            n=len(queue)
            lst=[node.val for node in queue]
            tmp=sum(lst)
            if tmp>max_sum:
                max_sum=tmp
                res=lvl
            for i in range(n):
                node =queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res
