class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        res = 0
        number_of_zeroes = 0
        for r in range(len(nums)):
            # צעד 1: הוספת האיבר החדש לחלון
            if nums[r] == 0:
                number_of_zeroes += 1
            # צעד 2: כיווץ החלון משמאל כל עוד חרגנו מכמות האפסים המותרת
            while number_of_zeroes > k:
                if nums[l] == 0:
                    number_of_zeroes -= 1
                l += 1
            # צעד 3: החלון עכשיו חוקי, בודקים אם שברנו שיא
            res = max(res, r - l + 1)
        return res