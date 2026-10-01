class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        while left + k < len(arr) and x - arr[left] > arr[left + k] - x:
            left += 1
        return arr[left:left + k]