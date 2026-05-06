class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} # key: number, value: index
        
        for i in range(len(nums)):
            n = target - nums[i]
            if n in hashmap:
                return [hashmap[n], i]
            hashmap[nums[i]] = i
        