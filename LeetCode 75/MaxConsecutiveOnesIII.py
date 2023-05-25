class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left:int=0
        right:int=0
        f:int=0
        tmp:int==0
        res:int=0
        while left<len(nums)-2 and nums[left]==0:
            left+=1
        right=left
        while right<len(nums)-1 and f<k+1:
            right+=1
            if nums[right]==0 and f<k+1:
                f+=1        
        if f==k+1:            
            right-=1
            f-=1
        tmp=right-left+1
        if left==len(nums)-2:
            print('gothere')
            tmp=k
            if nums[len(nums)-2]==1:
                tmp+=1
            if nums[len(nums)-1]==1:
                tmp+=1
            tmp=min(len(nums),tmp)

        if tmp>res:
            res=tmp
 
        while right<len(nums)-2 and f<k+1:
            if nums[left]==1:
                tmp-=1
            else:
                f-=1
                tmp-=1
            left+=1
            while right<len(nums)-1 and f<k+1:

                right+=1
                if nums[right]==1:
                    tmp+=1
                elif f<k+1:
                    tmp+=1
                    f+=1
            if f==k+1:
                tmp-=1
                right-=1
                f-=1

            if tmp>res:
                res=tmp
        return res
