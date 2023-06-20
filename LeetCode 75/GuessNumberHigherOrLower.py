# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        res: int
        
        def binarySearch(start, end):         
            tmp:int = start+(end-start)//2          
            ans=guess(tmp)
            if end-start==1 and ans!=0:
                tmp = start + ceil((end-start)/2)
                ans=guess(tmp)

            if ans==0:                
                self.res=tmp
                return
            elif ans==1:
                return binarySearch(tmp, end)
                
            else:
                return binarySearch(start, tmp)
            return
                
          
        binarySearch(1,n)
        return self.res
