class Solution:
    def maxArea(self, height: List[int]) -> int:
        left:int=0
        right:int=len(height)-1
        volume:int=0
        while left<right:

            tmp = (right-left)*min(height[left], height[right])
 
            if tmp>volume:
                volume=tmp
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return volume
