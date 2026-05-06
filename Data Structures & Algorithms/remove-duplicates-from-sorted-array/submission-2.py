class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        unique = set()

        for n in nums:
            if n not in unique:
                nums[k] = n
                k += 1
            unique.add(n)
        return k
        