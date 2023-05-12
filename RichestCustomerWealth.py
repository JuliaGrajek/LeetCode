class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth: List[int]
        res: int
        wealth = [sum(x) for x in accounts]
        res =max(wealth)
        return res
