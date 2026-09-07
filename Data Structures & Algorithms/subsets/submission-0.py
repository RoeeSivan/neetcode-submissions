class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #we start with an empty res
        res = []
        #helper method
        def backtrack(start_index, current_subset):
        # 1. we add the current state to the result
            res.append(current_subset[:])
        # 2. we go over all the elements from the current index until the end
            for i in range(start_index, len(nums)):
            # (Choose)
                current_subset.append(nums[i])
            # backtracking
                backtrack(i + 1, current_subset)
                current_subset.pop()
        backtrack(0, [])
        return res