class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        res:int = nums.index(max(nums))
        return res
