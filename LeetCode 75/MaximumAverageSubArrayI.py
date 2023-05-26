class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left:int=0
        right:int=k-1
        res:int=-inf
        tmp:int=0
        while right<len(nums):
            if right==k-1:
                tmp = sum(nums[left:right+1])
            else:
                tmp+=nums[right]
                tmp-=nums[left-1]
            if tmp>res:                
                res=tmp
       
            left+=1
            right+=1
        res=res/k
        return res
