class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = {}
        L = 0
        res = 0
        total = 0

        for R in range(len(s)):
            hashmap[s[R]] = 1 + hashmap.get(s[R], 0)

            total += 1
            maxNum = max(hashmap.values())
            
            while (total - maxNum) > k:
                hashmap[s[L]] -= 1
                L+=1
                total -= 1
                maxNum = max(hashmap.values())
            
            res = max(res, (R- L + 1))
        return res
            

                