class Solution:
    def countBits(self, n: int) -> List[int]:
        res: List[int] = []
    
        for i in range(n+1):
            res.append(bin(i)[2:].count('1'))
        return res
