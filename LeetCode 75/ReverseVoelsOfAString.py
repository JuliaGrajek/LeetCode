class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels=['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        left:int=0
        right:int=len(s)-1
        res=list(s)
        while left< right:
            if s[left] in vowels and s[right] in vowels:
                res[left], res[right] = s[right], s[left]
                left+=1
                right-=1
            elif s[left] in vowels and s[right] not in vowels:
                right-=1
            elif s[right] in vowels and s[left] not in vowels:
                left+=1
            else:
                right-=1
                left+=1
        return "".join(res)
