# Last updated: 2/25/2026, 3:35:34 PM
class Solution:
    def processStr(self, s: str) -> str:
        res = ""
        for l in s:
            if l == '*':
                if len(res) - 1 in range(len(res)):
                    res = res[0:len(res)-1]
            elif l == '#':
                res = res + res
            elif l == '%':
                res = res[::-1]
            else:
                res = res + str(l)
        return res