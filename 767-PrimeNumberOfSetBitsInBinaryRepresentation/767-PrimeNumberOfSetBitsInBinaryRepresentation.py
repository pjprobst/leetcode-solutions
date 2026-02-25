# Last updated: 2/25/2026, 3:35:53 PM
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        count = 0
        for i in range(left, right+1):
            if self.isPrime(bin(i).count("1")):
                count += 1
        return count
    def isPrime(self, num: int) -> bool:
        if num <= 1:
            return False
        elif num <= 3:
            return True
        elif num % 2 == 0 or num % 3 == 0:
            return False
        else:
            j = 5
            while j * j <= num:
                if num % j == 0 or num % (j + 2) == 0:
                    return False
                j += 6
        return True