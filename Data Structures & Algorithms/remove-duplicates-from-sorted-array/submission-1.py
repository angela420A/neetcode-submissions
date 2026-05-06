class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        unique = set()
        
        for i in range(len(nums)):
            if nums[i] not in unique:
                nums[k] = nums[i]
                k+=1
            unique.add(nums[i])
        return k