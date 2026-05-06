class Solution:
    def climbStairs(self, n: int) -> int:
        # DP cache ways
        one, two = 1, 1
        for i in range(n - 1):
            temp = one
            one += two
            two = temp
        return one