class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = [] #current permutation
        used = [False] * len(nums)
        nums = sorted(nums)
        def backtrack(path):
            if len(path) == len(nums):
                res.append(path.copy())
                return
            for i in range(len(nums)):
                # מקרה ראשון: האיבר כבר נמצא במסלול הנוכחי
                if used[i]:
                    continue
                # מקרה שני: האיבר זהה לקודם, והקודם לא בשימוש כרגע (מניעת ענף כפול)
                if i > 0 and nums[i] == nums[i-1] and used[i-1] == False:
                    continue
                path.append(nums[i])
                used[i] = True
                backtrack(path)
                used[i] = False
                path.pop()
                
        backtrack(path)
        return res