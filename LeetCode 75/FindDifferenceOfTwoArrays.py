class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        res1:List[int]=[]
        res2:List[int]=[]
        res1=[x for x in nums1 if x not in nums2]
        res2=[x for x in nums2 if x not in nums1]
        res1=list(set(res1))
        res2=list(set(res2))
        return [res1, res2]
