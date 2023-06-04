# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
       
        curr_sum:int=0
        self.res:int=0
        prefix_sums=defaultdict(int)

        def dfs(node: Optional[TreeNode],curr_sum:int, targetSum:int) ->int:

            if not node:
                return 0

            curr_sum+=node.val
            if curr_sum==targetSum:
                self.res+=1

            if prefix_sums.get(curr_sum-targetSum):
   
                self.res+=prefix_sums[curr_sum-targetSum]

            prefix_sums[curr_sum]+=1
            dfs(node.left, curr_sum, targetSum)
            dfs(node.right,curr_sum, targetSum)

            if prefix_sums[curr_sum]:
                prefix_sums[curr_sum]-=1
            return self.res

         
        return dfs(root, curr_sum, targetSum)
