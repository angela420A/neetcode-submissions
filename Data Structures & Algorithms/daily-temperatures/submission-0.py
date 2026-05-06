class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                j, pretemp = stack.pop()
                res[j] = i - j
            stack.append((i, temp))
        return res
        

