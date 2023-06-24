class Solution:
    def numTilings(self, n: int) -> int:
        self.cache: Dict[int, int]={}

        def dp(n:int)->int:
            if n==1:
                return 1
            elif n==2:
                return 2
            elif n==3:
                return 5
            elif n in self.cache:
                return self.cache[n]
            else:
                self.cache[n]=(2*dp(n-1)+dp(n-3))%(1e9+7)
                return self.cache[n]
        
        return int(dp(n))
