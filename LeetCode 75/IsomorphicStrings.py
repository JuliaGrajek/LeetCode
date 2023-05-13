from collections import Counter


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
            for  c in set(s):
                idxs = [i for i, ltr in enumerate(s) if ltr == c]
                idxt = [i for i, ltr in enumerate(t) if ltr == t[idxs[0]]]
                if idxs!=idxt:
                    return False
            return True
