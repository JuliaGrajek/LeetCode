class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        tmp: List[List[int]] = sorted(points, key =lambda s:s[1])
        res: int = 0
        currmax: int = -inf
        for i in tmp:
            if i[0]>currmax:
                res+=1
                currmax=i[1]
        return res
