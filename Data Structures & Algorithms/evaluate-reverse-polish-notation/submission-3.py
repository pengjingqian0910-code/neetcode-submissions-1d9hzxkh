class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] in "+-*/":
                b = int(stack.pop())
                a = int(stack.pop())
                if tokens[i] == "+":
                    result = a + b 
                elif tokens[i] == "-":
                    result = a - b
                elif tokens[i] == "*":
                    result = a * b
                else:
                    result = int(a / b)
                stack.append(result)
            else:
                stack.append(int(tokens[i]))
        return stack[0]    
                    