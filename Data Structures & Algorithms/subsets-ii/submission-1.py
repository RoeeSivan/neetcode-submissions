class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = [] #current permutation
        nums = sorted(nums)
        def backtrack(start_index,path):
            res.append(path.copy())
            for i in range(start_index,len(nums)):
                if i > start_index and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                backtrack(i+1,path)
                path.pop()
        backtrack(0,path)
        return res     

