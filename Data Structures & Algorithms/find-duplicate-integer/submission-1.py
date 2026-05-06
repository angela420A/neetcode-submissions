class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # the value is < len(nums) so and 1 ~ n: index
        # if the val == index, then like linked list has the next poiner.
        slow, fast = nums[0], nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = nums[0]
        while slow2 != slow:
            slow2 = nums[slow2]
            slow = nums[slow]
        return slow2