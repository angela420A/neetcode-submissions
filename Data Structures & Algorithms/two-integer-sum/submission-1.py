class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        existed = {} # key: number, val: index

        for i in range(len(nums)):
            num = target - nums[i]
            if num in existed:
                return [existed[num], i]
            existed[nums[i]] = i