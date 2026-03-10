# Last updated: 3/10/2026, 5:52:02 PM
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                if (i-1 not in range(len(flowerbed)) or flowerbed[i-1] == 0) and (i+1 not in range(len(flowerbed)) or flowerbed[i+1] == 0):
                    count += 1
                    flowerbed[i] = 1

        if count >= n:
            return True
        return False

