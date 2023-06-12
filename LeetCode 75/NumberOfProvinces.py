class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        self.visited: List[int] = []
        res: int = 0

        def findProvinceMembers(self, node:int, isConnected:List[List[int]]):
            for i,j  in enumerate(isConnected[node]):
                if j==1 and i not in self.visited:
                    self.visited.append(i)
                    findProvinceMembers(self, i, isConnected)
            return None
        for i in range(len(isConnected)):
            if i not in self.visited:
                res+=1
                findProvinceMembers(self, i, isConnected)
        return res
