class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        leng, res = 0, 0
        for n in nums:
            leng = leng + 1 if n else 0
            res = max(res, leng)
        return res