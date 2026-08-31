class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        size = len(flowerbed)
        for i in range(size):
            if flowerbed[i] == 0:
                isLeftEmpty  = (i == 0) or (flowerbed[i-1] == 0)
                isRightEmpty = (i == size - 1) or (flowerbed[i+1] == 0)
                if isLeftEmpty and isRightEmpty:
                    flowerbed[i] = 1
                    n -= 1
                    if n <= 0:
                        return True
        return n <= 0