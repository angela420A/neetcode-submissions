class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l < r:
            while l < r and not self.check(s[l]):
                l+=1
            while l < r and not self.check(s[r]):
                r-=1
            if s[l].lower() != s[r].lower():
                return False
            l+=1
            r-=1
        return True
        
    def check(self, word: str) -> bool:
        if (
            (ord('a') <= ord(word) and ord(word) <= ord('z')) or
            (ord('A') <= ord(word) and ord(word) <= ord('Z')) or
            (ord('0') <= ord(word) and ord(word) <= ord('9'))
        ):  return True
        return False