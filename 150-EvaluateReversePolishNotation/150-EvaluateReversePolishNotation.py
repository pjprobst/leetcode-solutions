# Last updated: 3/10/2026, 5:52:09 PM
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        '''
        ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
        ["10","6", 12,"-11","*","/","*","17","+","5","+"]
        ["10","6", -132,"/","*","17","+","5","+"]
        ["10", 0, "*","17","+","5","+"]
        [0,"17","+","5","+"]
        ["17","5","+"]
        ["22"]
        '''
        res = []
        for token in tokens:
            if token == '+':
                var2 = res.pop()
                var1 = res.pop()
                res.append(var1 + var2)
            elif token == '-':
                var2 = res.pop()
                var1 = res.pop()
                res.append(var1 - var2)
            elif token == '*':
                var2 = res.pop()
                var1 = res.pop()
                res.append(var1 * var2)
            elif token == '/':
                var2 = res.pop()
                var1 = res.pop()
                res.append(int(var1/var2))
            else:
                res.append(int(token))
        return res[0]