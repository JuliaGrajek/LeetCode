class Solution:
    def compress(self, chars: List[str]) -> int:
        first:int=0
        last:int=1
        first_free:int=0
        k:str=''
        
        while last < len(chars):

            if chars[first+1]!=chars[first]:
                chars[first_free]=chars[first]
                first=last
                first_free+=1
                last=first+1
                
            else: 
                while last<len(chars) and chars[last]==chars[first]:
                    last+=1
                k=str(last-first)
                chars[first_free]=chars[first]
                first_free+=1
                for i in range(len(k)):
                    chars[first_free]=k[i]
                    first_free+=1                
                first=last
                last=first+1
        if first==len(chars)-1:
            chars[first_free]=chars[first]
            first_free+=1
            
            # print(first_free)
        del chars[first_free:]
        return len(chars)
                    
