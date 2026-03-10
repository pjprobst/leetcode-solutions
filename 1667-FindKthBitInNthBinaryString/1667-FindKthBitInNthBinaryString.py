# Last updated: 3/10/2026, 5:51:51 PM
class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        si = ""
        si_prev = "0"
        '''
        possible = 1
        for i in range(n):
            possible = (possible + 1 + possible)
        if k not in range(possible):
            return -1
        '''
        while k-1 not in range(len(si)):
            si = (si_prev + "1" + (self.invert(si_prev))[::-1])
            si_prev = si
        return si[k-1]

    def invert(self, string: str) -> str:
        t = str.maketrans('01', '10')
        inverted_s = string.translate(t)
        return inverted_s