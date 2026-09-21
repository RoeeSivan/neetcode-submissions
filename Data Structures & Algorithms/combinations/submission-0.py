class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        path = []
        # k is the number of numbers chosen from the range
        def backtrack(start, path):
            if len(path) == k:
                res.append(path.copy())
                return
            
            for i in range(start, n+1):
                
                path.append(i)
                backtrack(i+1,path)
                path.pop()
                
        # Start the backtracking process
        backtrack(1, path)
        return res 