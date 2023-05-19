lass Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatestCandies = max(candies)
        res:List[bool]=[]
        for i in range(len(candies)):
            tmp = candies[i]+extraCandies
            if tmp>=greatestCandies:
                res.append(True)
            else:
                res.append(False)
        return res
