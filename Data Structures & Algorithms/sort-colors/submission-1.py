class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) == 0:
            return None
        return self.mergeSort(nums, 0, len(nums) - 1)
    
    def mergeSort(self, arr, l, r):
        if r - l + 1 <= 1:
            return arr
        
        mid = (l + r) // 2
        self.mergeSort(arr, l, mid)
        self.mergeSort(arr, mid + 1, r)

        self.merge(arr, l, mid, r)
        return arr
    
    def merge(self, arr, l, mid, r):
        L = arr[l : mid + 1]
        R = arr[mid + 1 : r + 1]

        i, j = 0, 0
        k = l

        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
        return arr
