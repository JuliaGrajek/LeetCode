class Solution:
    def longestPalindrome(self, s: str) -> int:
        occured = {}
        res = 0
        uneven=False
        for c in s:
            if c in occured:
                occured[c]+=1
            else:
                occured[c]=1
        for k,v in occured.items():
            res+=floor(v/2)*2
            if v%2!=0:
                uneven=True
        if uneven==True:
            res+=1
        return res
