# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if not pairs or len(pairs) == 0:
            return pairs
        return self.merge(pairs, 0, len(pairs)-1)

    def merge(self, arr, l, r):
        if r - l + 1 <= 1:
            return arr
        
        mid = (r + l) // 2
        self.merge(arr, l, mid)
        self.merge(arr, mid + 1, r)

        self.sort(arr, l, mid, r)
        return arr
    
    def sort(self, arr, l, m, r):
        L = arr[l : m + 1]
        R = arr[m + 1 : r + 1]
        
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

