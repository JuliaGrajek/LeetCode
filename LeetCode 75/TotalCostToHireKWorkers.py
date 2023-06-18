class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:

        res:int = 0
        c1:int = 0
        c2:int = 0
        end_first:int = candidates
        start_last:int = len(costs)-candidates-1
        first = costs[0:candidates]
        last = costs[max(candidates,len(costs)-candidates):]
        heapq.heapify(first)
        heapq.heapify(last)

        for i in range(k):

            if not last or (first and first[0]<=last[0]):
                res+=heapq.heappop(first)
                if end_first<=start_last:
                    heapq.heappush(first, costs[end_first])
                    end_first+=1
                            
            else:       
                res+=heapq.heappop(last)
                if end_first<=start_last:
                    heapq.heappush(last, costs[start_last])
                    start_last-=1   

        return res
