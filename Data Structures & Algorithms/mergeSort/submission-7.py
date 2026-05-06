# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if not pairs or len(pairs) == 0:
            return []
        return self.merge(pairs, 0, len(pairs) - 1)

    def merge(self, arr, s, e):
        if (e - s + 1) <= 1:
            return arr
        
        mid = (s + e) // 2
        self.merge(arr, s, mid)
        self.merge(arr, mid + 1, e)

        self.mergeTwoArr(arr, s, mid, e)
        return arr
    
    def mergeTwoArr(self, arr, s, mid, e):
        a1 = arr[s : mid + 1]
        a2 = arr[mid + 1 : e + 1]

        i, j = 0, 0
        k = s

        while i < len(a1) and j < len(a2):
            if a1[i].key <= a2[j].key:
                arr[k] = a1[i]
                i += 1
            else:
                arr[k] = a2[j]
                j += 1
            k+=1
        
        while i < len(a1):
            arr[k] = a1[i]
            i+=1
            k+=1
        while j < len(a2):
            arr[k] = a2[j]
            j+=1
            k+=1