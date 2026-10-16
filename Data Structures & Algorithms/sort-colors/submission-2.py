class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        sort = [0] * (max(nums) + 1)
        for n in nums:
            sort[n] += 1
        
        k = 0
        for i in range(len(sort)):
            for j in range(sort[i]):
                nums[k] = i
                k += 1
        