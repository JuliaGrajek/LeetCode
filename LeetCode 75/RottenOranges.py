class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dirs = ((1,0), (-1, 0), (0,1), (0,-1))
        rows, cols = len(grid), len(grid[0])

        no_fresh_oranges = reduce(lambda x,y: x+y, grid).count(1)
 
        if no_fresh_oranges==0:
            return 0

        def findRottenOranges(self, grid:List[List[int]]):
            rotten=[]
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j]==2:
                        rotten.append((i,j))
            return rotten

        rotten= findRottenOranges(self, grid)

        
        
        queue = collections.deque()
        for r in rotten:
            queue.append([r[0], r[1], 0])
          
        while queue:
            curr_i, curr_j, curr_t = queue.popleft()
            print((curr_i, curr_j, curr_t, no_fresh_oranges))
            for d in dirs:
                
                next_i = curr_i + d[0]
                next_j = curr_j + d[1]

                if 0<=next_i<rows and 0<=next_j<cols and grid[next_i][next_j]==1:
                    grid[next_i][next_j]=2
                    no_fresh_oranges-=1
                    if no_fresh_oranges==0:
                        return curr_t+1
                    queue.append([next_i, next_j, curr_t+1])
        return -1
