class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # valid tree - no cycles
        preMap = {i: [] for i in range(n)}
        for a, b in edges:
            # the graph is undirected thus we need to append both ends
            preMap[a].append(b)
            preMap[b].append(a)

        # visitSet = all vertices that were visited
        visitSet = set()

        def dfs(node,prev):
            if node in visitSet:
                return False
            visitSet.add(node)
            for nei in preMap[node]: # nei is every neighbor of node
                if nei == prev:
                    continue
                if not dfs(nei,node):
                    return False
            return True

        return dfs(0, -1) and len(visitSet) == n    

        #the dfs has 2 main roles: 1. to check that there are no circles. 2. fill up visitSet with every node we can reach from 0.
