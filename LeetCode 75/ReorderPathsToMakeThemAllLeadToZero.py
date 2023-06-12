class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u,v in connections:
            graph[u].append((v,1))
            graph[v].append((u,0))

        def countEdgesToBeFlipped(node:int, parent:int,graph:Dict[int, List[int]])->int:
            return sum(cost + countEdgesToBeFlipped(child, node, graph) for child, cost in graph[node] if child!=parent)

        return countEdgesToBeFlipped(0, -1, graph)
