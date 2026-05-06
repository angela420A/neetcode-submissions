class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = set()
        res = 0
        l, r = 0, 0

        while r < len(s):
            while s[r] in hashset:
                hashset.remove(s[l])
                l+=1
            hashset.add(s[r])
            res = max(res, r - l + 1)
            r+=1
        return res