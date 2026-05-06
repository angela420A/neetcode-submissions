# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        if not pairs or len(pairs) == 0:
            return []
        return self.sort(pairs, 0, len(pairs) - 1)
    
    def sort(self, arr, l, r):
        if r - l + 1 <= 1:
            return arr
        
        pivot = arr[r]
        left = l

        for i in range(l, r):
            if arr[i].key < pivot.key:
                temp = arr[left]
                arr[left] = arr[i]
                arr[i] = temp
                left += 1

        arr[r] = arr[left]
        arr[left] = pivot
        
        self.sort(arr, l, left - 1)
        self.sort(arr, left + 1, r)

        return arr