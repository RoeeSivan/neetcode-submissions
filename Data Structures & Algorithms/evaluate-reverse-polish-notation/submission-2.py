class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #brute force
        stack = []
        for token in tokens:
            if token == "+":
                #order does not matter when adding
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                b, a = stack.pop(), stack.pop()
                stack.append(a-b)
            elif token == '*':
                #order does not matter when multiplying
                stack.append(stack.pop() * stack.pop())
            elif token == '/':
                b, a = stack.pop(), stack.pop()
                stack.append(int(a/b))
            else:
                stack.append(int(token))
        return stack[0]
