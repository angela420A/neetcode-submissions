# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.devide(pairs, 0, len(pairs)-1)
    
    def devide(self, pairs, s, e):
        if (e - s + 1 <=1):
            return pairs
        
        m = (s + e) // 2
        self.devide(pairs, s, m)
        self.devide(pairs, m+1, e)

        self.merge(pairs, s, m, e)
        return pairs

    def merge(self, pairs, s, m, e):
        L = pairs[s : m+1]
        R = pairs[m+1 : e+1]

        i = 0
        j = 0
        k = s

        while i < len(L) and j < len(R):
            if L[i].key <= R[j].key:
                pairs[s] = L[i]
                i+=1
            else:
                pairs[s] = R[j]
                j+=1
            s+=1
        
        while i < len(L):
            pairs[s] = L[i]
            s+=1
            i+=1
        while j < len(R):
            pairs[s] = R[j]
            s+=1
            j+=1
        # return pairs