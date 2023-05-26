class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        flag:int=0
        left:int=0
        right:int=0
        while right<len(nums):
            right+=1
            if nums[right-1]==0:
                print('got here')
                flag+=1
            if flag>1:
                if nums[left]==0:
                    flag-=1
                left+=1
        return right-left-1
