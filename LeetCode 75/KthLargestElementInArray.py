import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res:int
        heapq.heapify(nums)
        if len(nums)==1:
            return nums[0]
        for i in range(len(nums)-k+1):
            res = heapq.heappop(nums)

        return res
