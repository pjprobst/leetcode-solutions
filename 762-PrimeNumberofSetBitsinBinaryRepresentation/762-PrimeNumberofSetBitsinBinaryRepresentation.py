# Last updated: 2/21/2026, 12:38:24 PM
1class Solution:
2    def countPrimeSetBits(self, left: int, right: int) -> int:
3        count = 0
4        for i in range(left, right+1):
5            if self.isPrime(bin(i).count("1")):
6                count += 1
7        return count
8    def isPrime(self, num: int) -> bool:
9        if num <= 1:
10            return False
11        elif num <= 3:
12            return True
13        elif num % 2 == 0 or num % 3 == 0:
14            return False
15        else:
16            j = 5
17            while j * j <= num:
18                if num % j == 0 or num % (j + 2) == 0:
19                    return False
20                j += 6
21        return True