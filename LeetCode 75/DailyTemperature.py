class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer: List[int] = [0]*len(temperatures)
        stack = []
  
        for idx, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                top_pos, top_val = stack.pop()
                answer[top_pos]=idx-top_pos
            stack.append((idx, t))
        return answer
            
