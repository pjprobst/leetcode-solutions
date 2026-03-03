# Last updated: 3/3/2026, 12:50:52 AM
1class Solution:
2    def findKthBit(self, n: int, k: int) -> str:
3        si = ""
4        si_prev = "0"
5        '''
6        possible = 1
7        for i in range(n):
8            possible = (possible + 1 + possible)
9        if k not in range(possible):
10            return -1
11        '''
12        while k-1 not in range(len(si)):
13            si = (si_prev + "1" + (self.invert(si_prev))[::-1])
14            si_prev = si
15        return si[k-1]
16
17    def invert(self, string: str) -> str:
18        t = str.maketrans('01', '10')
19        inverted_s = string.translate(t)
20        return inverted_s