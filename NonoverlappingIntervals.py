class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        tmp: List[List[int]] = sorted(intervals, key= lambda s: (s[1]))
        print(tmp)
        currmax:int = -5*10**4-1
        res:int = 0
        for i in tmp:
            if i[0]<currmax:
   
                res+=1
            else:
                currmax=i[1]
        return res
