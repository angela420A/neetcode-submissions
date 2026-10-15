class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        n1, n2 = nums1[:m], nums2[:n]

        i, j = 0, 0
        k = 0
        
        while i < len(n1) and j < len(n2):
            if n1[i] <= n2[j]:
                nums1[k] = n1[i]
                i += 1
            else:
                nums1[k] = n2[j]
                j += 1
            k += 1
        
        while i < len(n1):
            nums1[k] = n1[i]
            i += 1
            k += 1
        
        while j < len(n2):
            nums1[k] = n2[j]
            j += 1
            k += 1