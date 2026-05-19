class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        existed = set()
        for n in nums:
            if n in existed:
                return True
            existed.add(n)
        return False
