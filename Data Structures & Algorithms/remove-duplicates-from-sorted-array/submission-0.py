class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k, i = 0, 0
        while i < len(nums):
            if k == 0 or nums[i] != nums[k-1]:
                nums[k] = nums[i]
                k+=1
            i+=1
        return k
                
            