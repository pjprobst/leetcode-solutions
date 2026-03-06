# Last updated: 3/6/2026, 9:54:25 AM
1class Solution:
2    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
3        count = 0
4        for i in range(len(flowerbed)):
5            if flowerbed[i] == 0:
6                if (i-1 not in range(len(flowerbed)) or flowerbed[i-1] == 0) and (i+1 not in range(len(flowerbed)) or flowerbed[i+1] == 0):
7                    count += 1
8                    flowerbed[i] = 1
9
10        if count >= n:
11            return True
12        return False
13
14