
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res:List[int]=[]
        tmp:int=1
        prefix:List[int] =len(nums)*[1]
        suffix:List[int]=len(nums)*[1]
        p:int=1
        s:int=1
       
        for i in range(0,len(nums)):
            prefix[i]=p
            p*=nums[i]
        for i in range(len(nums)-1, -1, -1):
            suffix[i]=s
            s*=nums[i]

        res.append(suffix[0])
        for i in range(1, len(nums)-1):
            res.append(prefix[i]*suffix[i])
        res.append(prefix[len(nums)-1])

        return res
    
        
