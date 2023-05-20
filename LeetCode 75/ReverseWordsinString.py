class Solution:
    def reverseWords(self, s: str) -> str:
        words:List[str]=[]
        i:int=0
        end:int=0
        word:str=''
        while i<len(s):

            if s[i]!=' ':
                word+=s[i]
            if word!='' and s[i]==' ':
                words.append(word)
                word=''
            i+=1
        if word!='':
            words.append(word)
            word=''
    
        for j in range(1,len(words)):
            word+=words[-j]+' '
        word+=words[0]
        return word
