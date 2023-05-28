class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        dict1:Dict[int, List[int]]={}
        dict2:Dict[int, List[int]]={}
        res:int=0
        for i,r in enumerate(grid):
            dict1[i]=r

        for j in range(len(grid)):
            c=[row[j] for row in grid]
            dict2[j]=c
  
        for n in list(dict1.values()):
            for m in list(dict2.values()):
                if n==m:
                    res+=1
        return res
