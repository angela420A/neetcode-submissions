class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        hashset = set()
        l, r = 0, 0

        while r < len(s):
            while s[r] in hashset:
                hashset.remove(s[l])
                l += 1
            res = max(res, r - l + 1)
            hashset.add(s[r])
            r += 1
        return res
            