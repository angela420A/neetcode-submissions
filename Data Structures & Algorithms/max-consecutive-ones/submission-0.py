class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        length, res = 0, 0
        for n in nums:
            if n == 1:
                length += 1

            res = max(res, length)
            if n == 0:
                length = 0
        return res