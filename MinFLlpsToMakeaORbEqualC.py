class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        res:int = 0
        tmp = a | b
        if tmp==c:
            return 0
        tmp = tmp^c
        tmp2 = tmp&c
        res+=bin(tmp).count('1')
        res+=bin((a&b)&(~c)).count('1')
        return res
