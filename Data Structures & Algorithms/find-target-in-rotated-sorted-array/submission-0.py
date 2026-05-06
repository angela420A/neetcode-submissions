class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        
        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return m
        
            # Check left
            if nums[l] <= nums[m]:
                # target in right group
                if target < nums[l] or nums[m] < target:    
                    l = m + 1
                # target in left group
                else:
                    r = m - 1

            # Check right
            else:
                # target in left group
                if target < nums[m] or nums[r] < target:
                    r = m - 1
                # target in right group
                else:
                    l = m + 1
        return -1
            

#         [3,4,5,6,1,2]
#              | 
#                  | 

#  ...... [5,6,1,2,3,4]
#              | 
#                  | 
#                    | 
        
#         if nums[m] > num[l]
#             if target < nums[l] or nums[m] < target:
#                 l = m + 1
#             else:
#                 r = m - 1
    
#         else nums[m] < nums[r]
#             if target < nums[m] or nums[r] < target:
#                 r = m - 1
#             else:
#                 l = m + 1

