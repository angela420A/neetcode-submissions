class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0] * 3
        for n in nums:
            counts[n] += 1
        
        i = 0
        for j in range(len(counts)):
            c = counts[j]

            while c > 0:
                nums[i] = j
                c -= 1
                i += 1