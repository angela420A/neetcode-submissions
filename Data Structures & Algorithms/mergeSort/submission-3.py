# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if not pairs or len(pairs) == 0:
            return []
        return self.sort(pairs, 0, len(pairs)-1)
    
    def sort(self, arr, l, r):
        if r - l + 1 <= 1:
            return arr

        mid = (l + r) // 2
        self.sort(arr, l, mid)
        self.sort(arr, mid + 1, r)

        self.merge(arr, l, mid, r)
        return arr
    
    def merge(self, arr, l, mid, r):
        L = arr[l: mid + 1]
        R = arr[mid + 1: r + 1]

        i, j = 0, 0
        k = l

        while i < len(L) and j < len(R):
            if L[i].key <= R[j].key:
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
        
        