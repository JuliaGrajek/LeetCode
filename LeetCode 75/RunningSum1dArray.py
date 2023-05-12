class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res: List[int]
        res = [sum(nums[0:i]) for i in range(1,len(nums)+1)]
        return res
