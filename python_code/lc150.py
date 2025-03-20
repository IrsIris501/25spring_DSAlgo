class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        symbols={'+', '-', '*', '/'}
        stack=[]
        for i in tokens:
            if i in symbols:
                b=stack.pop()
                a=stack.pop()
                if i=='+':
                    stack.append(a+b)
                elif i=='-':
                    stack.append(a-b)
                elif i=='*':
                    stack.append(a*b)
                else:
                    stack.append(int(a/b))
            else:
                stack.append(int(i))
        return stack[0]
