class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = { "]":"[", "}":"{", ")":"(" }
        stack = []

        for b in s:
            if b in hashmap:
                if stack and hashmap[b] == stack.pop():
                    continue
                else:
                    return False
            stack.append(b)
        return len(stack) == 0