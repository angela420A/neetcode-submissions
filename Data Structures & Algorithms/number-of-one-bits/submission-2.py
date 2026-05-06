class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            # The way to ignore all the 0 bit
            n &= (n - 1)
            res += 1
        return res