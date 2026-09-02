class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in range(len(operations)):
            op = operations[i]
            try:
                op = int(op)
                stack.append(op)
            except:
                if op == '+':
                    print(stack)
                    op2 = stack.pop()
                    op1 = stack.pop()
                    op3 = op1 + op2
                    stack.append(op1)
                    stack.append(op2)
                    stack.append(op3)
                elif op == 'D':
                    op1 = stack.pop()
                    op2 = op1*2
                    stack.append(op1)
                    stack.append(op2)
                elif op == 'C':
                    stack.pop()
        num = 0
        for i in range(len(stack)):
            num += stack.pop()
        return num
