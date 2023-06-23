class Solution:
    def tribonacci(self, n: int) -> int:
        self.cached:Dict[int,int]={0:0, 1:1, 2:1}

        def recursiveTribonacci(self,n:int)->int:
            if n in self.cached:
                return self.cached[n]
            else:
                res= recursiveTribonacci(self,n-1)+recursiveTribonacci(self,n-2)+recursiveTribonacci(self,n-3)
                self.cached[n]=res
                return res

        return recursiveTribonacci(self,n)
