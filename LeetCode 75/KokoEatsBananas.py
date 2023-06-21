class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        right:int=max(piles)
        left:int=1
        mid:int=1
        tmp:bool=0

        def canEatBananas(k:int, piles : List[int], h:int)->bool:
            hours_needed = [ceil(x/k) for x in piles]
            return sum(hours_needed)<=h

        while right>left:
            mid = (right+left)//2

            tmp = canEatBananas(mid, piles,h)
            if tmp:
                right=mid
            else:
                left = mid+1
        return right
