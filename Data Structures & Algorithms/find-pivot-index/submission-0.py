class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        total = sum(nums)

        for i in range(len(nums)):
            povit = nums[i]
            right = total - left - povit

            if left == right:
                return i
            else:
                left += povit
        return -1
