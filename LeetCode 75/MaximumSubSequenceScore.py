class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs: List[tuple]=[]
        heap: List[int]=[]
        currSum: int = 0

        for i in range(len(nums1)):
            pairs.append((nums1[i], nums2[i]))

        pairs = sorted(pairs, key= lambda x: x[1], reverse = True)
        heap = [x[0] for x in pairs[:k]]        
        currSum = sum(heap)
        heapq.heapify(heap)
        res = currSum*pairs[k-1][1]
       
        for j in range(k,len(nums1)):
            currSum-=heapq.heappop(heap)
            currSum+=pairs[j][0]
            heapq.heappush(heap, pairs[j][0])
            tmp = currSum*pairs[j][1]
            res = max(res, tmp)
        return res
