class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        high,low = max(piles),1
        ans = high
        while low <= high:
            mid = (high + low) //2
            # we need to calculate total hours needed at speed mid
            total_hours = 0
            for pile in piles:
                total_hours = total_hours + math.ceil(pile / mid)
            if total_hours <= h:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
