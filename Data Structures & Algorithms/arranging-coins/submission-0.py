class Solution:
    def arrangeCoins(self, n: int) -> int:
        l = 0
        r = n
        res = 0 
        while l <= r:
            mid = (l+r) // 2
            coins_needed = mid * (mid + 1) // 2
            
            if coins_needed == n:
                return mid
            elif coins_needed < n:
                res = mid
                l = mid + 1
            else:
                r = mid - 1 
        return res 