class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = {}
        res = 0
        L = 0

        for R in range(len(s)):
            hashmap[s[R]] = 1 + hashmap.get(s[R], 0)

            while (R - L + 1) - max(hashmap.values()) > k:
                hashmap[s[L]] -= 1
                L+=1
            
            res = max(res, R - L + 1)
            
        return res