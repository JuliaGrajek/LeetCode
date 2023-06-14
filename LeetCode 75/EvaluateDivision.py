from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        fin:List[float]=[]
        self.given_vals = defaultdict(list)
        self.weights = defaultdict(list)

        for i,eq in enumerate(equations):
            self.given_vals[eq[0]].append(equations[i])
            self.given_vals[eq[1]].append(equations[i])
            self.weights[eq[0]].append(values[i])
            self.weights[eq[1]].append(values[i])

        def evaluateDivision(self, q:List[str], res:int, path:List[str])->float:
            results=[]
            for i in range(len(self.given_vals[q[0]])):  
                eq=self.given_vals[q[0]][i]
                val = self.weights[q[0]][i]        
                
                if eq[0] not in path and eq[1] not in path:             
                    path1=path.copy()
                    path1.append(q[0])
                    
                    if eq[1]==q[1]:               
                        return res*val
                    elif eq[0]==q[1]:
                        return res/val
                    else:
                        if q[0]==eq[0]:
                            result= evaluateDivision(self,[eq[1], q[1]], res*val, path1)
                            if result is not None:
                                results.append(result)

                        else:
                            result= evaluateDivision(self, [eq[0], q[1]], res/val, path1)
                            if result is not None:
                                results.append(result)
            if len(results)>0:
                return max(results)
            else:
                return -1.0        
                    

        for q  in queries:
            if q[0] not in self.given_vals or q[1] not in self.given_vals:
                fin.append(-1.0)
            elif q[0]==q[1]:
                fin.append(1.0)
            else:
                tmp = evaluateDivision( self, q, 1,[])

                fin.append(tmp)
           
        return fin
