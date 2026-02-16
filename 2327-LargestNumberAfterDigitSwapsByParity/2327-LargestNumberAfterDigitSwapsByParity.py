# Last updated: 2/15/2026, 8:54:08 PM
class Solution:
    def largestInteger(self, num: int) -> int:
        even = []
        even_index = []
        odd = []
        odd_index = []
        for i,n in enumerate(str(num)):
            n = int(n)
            if n % 2 == 0:
                even.append(n)
                even_index.append(i)
            else:
                odd.append(n)
                odd_index.append(i)
        even = sorted(even, reverse=True)
        odd = sorted(odd, reverse=True)
        even_count = 0
        odd_count = 0
        res = 0
        for i in range(0, len(str(num))):
            if i in even_index:
                res += math.pow(10, len(str(num))-1-even_count-odd_count) * even[even_count]
                even_count += 1
            else:
                res += math.pow(10, len(str(num))-1-even_count-odd_count) * odd[odd_count]
                odd_count += 1
        return int(res)