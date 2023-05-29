class Solution:
    def removeStars(self, s: str) -> str:
        lst:List[str]=[]
        res:str=""
        for c in s:
            if c!='*':
                lst.append(c)
            else:
                lst.pop()
        for i in lst:
            res+=i
        return res
