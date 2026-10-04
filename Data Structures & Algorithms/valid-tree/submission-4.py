class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # valid tree - no cycles
        preMap = {i: [] for i in range(n)}
        for a, b in edges:
            # the graph is undirected thus we need to append both ends
            preMap[a].append(b)
            preMap[b].append(a)

        # visitSet = all courses along the current DFS path
        visitSet = set()

        def dfs(node,prev):
            if node in visitSet:
                return False
            visitSet.add(node)
            for pre in preMap[node]:
                if pre == prev:
                    continue
                if not dfs(pre,node):
                    return False
            return True

        return dfs(0, -1) and len(visitSet) == n    
