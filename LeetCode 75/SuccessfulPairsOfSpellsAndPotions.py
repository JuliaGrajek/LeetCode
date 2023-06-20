class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:

        potions.sort()
        res: List[int]=[]
        def getNumberOfPotions(spell:int, potions: List[int], success:int, start:int, end:int) -> int:

            res : int = 0
            while end > start:
                tmp =start+(end-start)//2
                success_tmp = potions[tmp]*spell
                if success_tmp<success:
                    start = tmp+1
                else:
                    if tmp==0 or potions[tmp-1]*spell<success:
                        return tmp
                    end=tmp-1
                return getNumberOfPotions(spell, potions, success, start, end)
            if potions[start]*spell>=success:

                return start
            else:
                return None

        for spell in spells:        
            idx = getNumberOfPotions(spell, potions, success, 0, len(potions)-1)
            print(idx)
            if idx is None:
                res.append(0)
            else:            
                res.append(len(potions)-idx)

        return res
        
