class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        length, res = 0, 0
        for n in nums:
            if n == 0:
                res = max(res, length)
                length = 0
            else:
                length += 1
        return max(res, length)