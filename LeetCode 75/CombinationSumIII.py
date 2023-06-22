class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.numbers: List[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.res: List[List[int]] = []

        def backtrack(self,curr_sum:int, remaining_digits:List[int], k:int, n:int):
     
            if len(remaining_digits)==9-k:

                if curr_sum==n:
                    tmp = [x for x in self.numbers if x not in remaining_digits]
                    if tmp not in self.res:
                        self.res.append(tmp)
                return
            for i in remaining_digits:
                if i<=n-curr_sum:
                    remaining_digits2 = remaining_digits.copy()
                    remaining_digits2.remove(i)
                    backtrack(self, curr_sum+i,remaining_digits2, k, n)

     
        backtrack(self, 0, self.numbers,k, n)
        return self.res
