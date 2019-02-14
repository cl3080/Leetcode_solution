class Solution:
    def evalRPN(self, tokens: 'List[str]') -> 'int':
        stack = []
        for i in range(len(tokens)):
            if tokens[i] != '+' and tokens[i] != '-' and tokens[i] != '/' and tokens[i] !=  '*':
                stack.append(int(tokens[i]))
            else:
                a = stack.pop()
                b = stack.pop()
                if tokens[i] == '+':
                    stack.append(a+b)
                if tokens[i] == '-':
                    stack.append(b-a)
                if tokens[i] == '*':
                    stack.append(b*a)
                if tokens[i] == '/':
                    if a*b > 0:
                        stack.append(b//a)
                    else:
                        stack.append(-(-b//a))
        return stack[0]
