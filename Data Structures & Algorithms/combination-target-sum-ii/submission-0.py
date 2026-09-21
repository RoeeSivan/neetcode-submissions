class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates = sorted(candidates)
        path = []
    
        def backtrack(start_index, current_target):
            if current_target == 0:
                res.append(path.copy())
                return
            
            for i in range(start_index, len(candidates)):
                # skip duplicates at the same level of recursion
                if i > start_index and candidates[i] == candidates[i-1]:
                    continue
                # early exit if the number exceeds the remaining target
                if candidates[i] > current_target:     
                    break
                
                path.append(candidates[i])
                backtrack(i+1, current_target - candidates[i])
                path.pop()
                
        # Start the backtracking process
        backtrack(0, target)
        return res