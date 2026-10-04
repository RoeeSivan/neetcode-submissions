class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = n
        # we can also do par = list(range(n))
        par = [num for num in range(n)] #every node is the parent of itself
        # find returns the root of x
        def find(x):
            # if x is not its own parent, then x is not the root
            if  par[x] != x:
                # recursively find the root and assign it directly 
                # path compression
                par[x] = find(par[x])
            return par[x]

        def union(a,b):
            root_a,root_b = find(a), find(b)
            if root_a == root_b:
                return False
            par[root_b] = root_a
            return True
        for a,b in edges:
            if union(a,b):
                res -= 1
        return res
