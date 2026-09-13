class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # sum of first window
        target_sum = k * threshold
        window_sum, curr_sum = 0,0
        res = 0
        for num in range(k):
            window_sum += arr[num]
        if window_sum >= target_sum:
            res += 1
        for i in range(k,len(arr)):
            window_sum += arr[i]
            window_sum -= arr[i-k]
            if window_sum >= target_sum:
                res += 1
        return res
