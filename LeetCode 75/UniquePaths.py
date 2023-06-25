class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths: List[List[int]] = [[1 for j in range(m)] for i in range(n)]
        
        for i in range(1,n):
            for j in range(1, m):

                paths[i][j]= paths[i][j-1]+paths[i-1][j]
        
        return paths[n-1][m-1]
