# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        if not pairs:
            return []

        # creates a shallow copy of the entire
        res = [pairs[:]]
        for i in range(1, len(pairs)):
            j = i - 1
            while j >= 0 and pairs[j].key > pairs[j + 1].key:
                temp = pairs[j + 1]
                pairs[j + 1] = pairs[j]
                pairs[j] = temp
                j-=1
            res.append(pairs[:])
        return res