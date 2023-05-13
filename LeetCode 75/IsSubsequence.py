class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s)>len(t):
            return False
        if not set(s).issubset(set(t)):

            return False
        for c in s:
   
            try:
                idx=t.index(c)
   
            except:
                return False
            t=t[idx+1:]

        return True
