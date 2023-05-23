class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        tmp:int=0
        res:int = 0
        for n in gain:
            tmp+=n
            if tmp>res:
                res=tmp
        return res
