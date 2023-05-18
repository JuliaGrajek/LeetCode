class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word3=''
        j=0
        for i in range(min(len(word1), len(word2))):
            word3+=word1[i]+word2[i]
            j+=1
        if len(word1)>len(word2):
            word3+=word1[j:]
        else:
            word3+=word2[j:]
        return word3
