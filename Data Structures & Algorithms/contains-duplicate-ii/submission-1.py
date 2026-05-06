class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashset = set()
        l, r = 0, 0

        while r < len(nums):
            if abs(l - r) > k:
                hashset.remove(nums[l])
                l+=1
            
            if nums[r] in hashset:
                return True
            hashset.add(nums[r])
            r+=1
        return False
