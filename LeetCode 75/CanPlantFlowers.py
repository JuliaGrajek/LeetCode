import math as m
class Solution:
    def canPlaceFlowers(self,flowerbed: List[int], n: int) -> bool:
        
        i:int=0
        j:int=0
        flowerbed=[0]+flowerbed+[0]
        while i<len(flowerbed) and n>0:        
            
            if flowerbed[i]==0:
                j+=1
            if flowerbed[i]==1:
                n=max(0,n-m.ceil(j/2)+1)
                j=0
            i+=1

        if j>0 and n>0:
            n=max(0,n-m.ceil(j/2)+1)
        if n==0:
            return True
        else:
            return False
Console
