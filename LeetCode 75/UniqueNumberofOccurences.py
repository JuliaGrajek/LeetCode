class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurences:Dict[int,int]={}
        lst:List[int]=[]
        for i in arr:
            if i in occurences:
                occurences[i]+=1
            else:
                occurences[i]=1
         
        for key, value in occurences.items():
            if value not in lst:
                lst.append(value)
        if len(lst)==len(occurences):
            return True
        else:
            return False
