class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = { ")": "(", "]": "[", "}": "{" }
        for b in s:
            if b in match:
                if stack and stack.pop() == match[b]:
                    continue
                else:
                    return False
            stack.append(b)
        return True if len(stack) == 0 else False