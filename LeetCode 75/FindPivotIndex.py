class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        for i in range(len(nums)):
            if sum(nums[0:i])==sum(nums[i+1:]):
                return i
        return -1
      
      #to not calcaulate the entire sum every time
      def pivotIndex2(self, nums: List[int]) -> int:
        sumL=0
        sumR=sum(nums)
        for i in range(len(nums)):
            sumR-=nums[i]
            if sum(nums[0:i])==sum(nums[i+1:]):
                return i
            sumL+=nums[i]
        return -1
