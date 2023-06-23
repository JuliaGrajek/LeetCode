class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self.cache:Dict[int,int]={}
      

        def recursiveStep(self, cost:List[int], i:int) -> int:
   
            if i<2:
                return cost[i]
            elif i in self.cache:
                return self.cache[i]        
            else:
                self.cache[i]=cost[i]+min(recursiveStep(self, cost, i-1), recursiveStep(self, cost, i-2))
                return self.cache[i]
                
            
        res = min(recursiveStep(self, cost, len(cost)-1), recursiveStep(self, cost, len(cost)-2))
    
        return res
