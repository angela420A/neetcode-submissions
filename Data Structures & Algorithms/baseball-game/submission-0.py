class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op == "+":
                if stack and stack[-2]:
                    stack.append(stack[-1] + stack[-2])
            elif op == "D":
                if stack:
                    stack.append(stack[-1] *2)
            elif op == "C":
                if stack:
                    stack.pop()
            else:
                stack.append(int(op))
        return sum(stack)