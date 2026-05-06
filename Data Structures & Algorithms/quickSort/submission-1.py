# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        if not pairs or len(pairs) == 0:
            return pairs
        return self.divide(pairs, 0, len(pairs) - 1)
    
    def divide(self, pairs, s, e):
        # check if it rich the button or not
        if (e - s + 1) <= 1:
            return pairs
        
        pivot = pairs[e]
        l = s
        
        for i in range(s, e):
            if pairs[i].key < pivot.key:
                tmp = pairs[l]
                pairs[l] = pairs[i]
                pairs[i] = tmp
                l+=1
        pairs[e] = pairs[l]
        pairs[l] = pivot

        self.divide(pairs, s, l - 1)
        self.divide(pairs, l + 1, e)
        return pairs
        