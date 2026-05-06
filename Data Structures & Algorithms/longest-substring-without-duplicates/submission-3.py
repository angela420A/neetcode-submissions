class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        L = 0
        exist = set()

        for R in range(len(s)):
            while s[R] in exist:
                exist.remove(s[L])
                L+=1
            res = max(res, R - L + 1)
            exist.add(s[R])
        return res