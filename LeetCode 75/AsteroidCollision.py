class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        right:List[int]=[]
        a:int=0
        while a<len(asteroids):

            if asteroids[a]>0:

                right.append(asteroids[a])
                a+=1
            else: 
                if right==[] or right[-1]<0:
                    right.append(asteroids[a])
                    a+=1
                elif right[-1]==-asteroids[a]:
                    right.pop()
                    a+=1
                elif right[-1]<=-asteroids[a]:
                    right.pop()
                else:
                    a+=1
        
        return right
