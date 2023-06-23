class Solution:
    def rob(self, nums: List[int]) -> int:
        self.cache:Dict[int,int]={}

        def dp(h:int)->int:
            print(h)
            if h<0:
                return 0
            elif h<2:
                return nums[h]
            elif h in self.cache:
                return self.cache[h]
            else:
                self.cache[h] = nums[h]+max(dp(h-2), dp(h-3))
                return self.cache[h]
        
        res = max(dp(len(nums)-1), dp(len(nums)-2))
        return res
