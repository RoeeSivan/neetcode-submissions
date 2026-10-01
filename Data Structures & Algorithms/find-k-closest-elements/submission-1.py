class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(arr) - 1
        #shrink the window until its size equals k
        while (right - left +1) > k:
            #compare distances from the target to outer elements
            distance_left = abs(arr[left] - x)
            distance_right = abs(arr[right]- x)
            #move the pointer that points to the larger distance
            if distance_left > distance_right:
                left += 1
            else:
                right -= 1
        return arr[left:right+1]