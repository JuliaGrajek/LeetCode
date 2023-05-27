class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1)!=len(word2):
            return False
        letters1:Dict[str,int]={}
        letters2:Dict[str,int]={}

        def getLetterOccurences(str1:str) ->Dict[str,int]:
            res_dict = {}
            for c in str1:
                if c in res_dict:
                    res_dict[c]+=1
                else:
                    res_dict[c]=1
            return res_dict
        
        def getValuesList(dict1:Dict)->List:
            res=[]
            for key, value in dict1.items():
                res.append(value)
            return sorted(res)

    
        letters1 = getLetterOccurences(word1)
        letters2 = getLetterOccurences(word2)

        if set(letters1)!=set(letters2):
            return False
        
        values1 = getValuesList(letters1)
        values2 = getValuesList(letters2)
        
        if values1!=values2:
            return False
        return True
        
