class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==1:
            return 0
        res:int=0
        left:int=0
        right:int=1

        while right<len(prices):
     
            if prices[right]<prices[left]:
                left=right
                
            else:
                res = max(res, prices[right]-prices[left])
            right+=1
        return res
Console
