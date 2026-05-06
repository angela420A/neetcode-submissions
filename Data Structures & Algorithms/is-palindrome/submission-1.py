class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        
        while l < r:
            while l < r and not self.check(s[l]):
                l += 1
            while l < r and not self.check(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
    
    def check(self, w):
        if (
            (ord('a') <= ord(w) and ord(w) <= ord('z')) or
            (ord('A') <= ord(w) and ord(w) <= ord('Z')) or
            (ord('0') <= ord(w) and ord(w) <= ord('9'))
        ):  return True
        return False