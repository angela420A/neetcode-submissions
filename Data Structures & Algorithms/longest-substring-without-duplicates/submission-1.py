class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset= set()
        L, R = 0, 0
        res = 0

        while R < len(s):
            while s[R] in hashset:
                hashset.remove(s[L])
                L+=1
            res = max(res, (R - L + 1))
            hashset.add(s[R])
            R+=1
        return res