class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        self.visited:List[int]=[0]

        def visitRoomsRecursively(self,room:int, rooms:List[List[int]]):
            
            for i in rooms[room]:
               
                if i not in self.visited:
                    self.visited.append(i)
                    visitRoomsRecursively(self,i, rooms)
            return None
        
        visitRoomsRecursively(self,0, rooms)
        if len(self.visited)==len(rooms):
            return True
        else:
            return False
