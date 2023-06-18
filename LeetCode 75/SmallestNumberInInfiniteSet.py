class SmallestInfiniteSet:

    def __init__(self):
        self.isPresent = set()
        self.addedIntegers = []
        self.currentInteger = 1
        

    def popSmallest(self) -> int:
        if len(self.addedIntegers)>0:
            res = heapq.heappop(self.addedIntegers)
            self.isPresent.remove(res)
        else:
            res = self.currentInteger
            self.currentInteger+=1
        return res
        

    def addBack(self, num: int) -> None:
        if self.currentInteger <= num or num in self.isPresent:
            return
        heapq.heappush(self.addedIntegers, num)
        self.isPresent.add(num)
        
