class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        res=0
        tmp=0
        for j in range(k):
            if s[j] in vowels:
                tmp+=1
        res=tmp
        if tmp==k:
            return tmp
        for i in range(len(s)-k):
            if s[k+i] in vowels:
                tmp+=1
            if s[i] in vowels:
                tmp-=1
            if tmp>res:
                res=tmp
            
        return res
