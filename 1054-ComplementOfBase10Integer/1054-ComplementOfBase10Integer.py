# Last updated: 4/24/2026, 8:45:40 PM
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        binary = ""
        n = bin(n)[2:]
        for i in n:
            binary += str(1-int(i))
        return int(binary, 2)
