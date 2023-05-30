class Solution:
    def decodeString(self, s: str) -> str:
   
        curr_str:str=''
        num:int=0
        stack:List[str]=[]
        for c in s:
            if c.isdigit():
                num = num*10+int(c)            
            elif c=='[':
                stack.append(curr_str)
                stack.append(num)
               
                curr_str=''
                num=0                
            elif c==']':
                prev_num=stack.pop()
                prev_txt=stack.pop()
          
                curr_str = prev_txt+curr_str*prev_num
            else:
                curr_str+=c
        while stack:
            curr_str =stack.pop()+curr_str
        return curr_str
