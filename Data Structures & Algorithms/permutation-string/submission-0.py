class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        c1, c2 = [0]*26, [0]*26
        for i in range(len(s1)):
            c1[ord(s1[i]) - ord('a')] += 1
            c2[ord(s2[i]) - ord('a')] += 1
        
        isMatch = 0
        for i in range(26):
            isMatch += 1 if c1[i] == c2[i] else 0
        
        l = 0
        for r in range(len(s1), len(s2)):
            if isMatch == 26:
                return True
            
            idx = ord(s2[r]) - ord('a')
            c2[idx] += 1
            if c2[idx] == c1[idx]:
                isMatch += 1
            elif c2[idx] == c1[idx] + 1:
                isMatch -=1

            idx = ord(s2[l]) - ord('a')
            c2[idx] -= 1
            if c2[idx] == c1[idx]:
                isMatch += 1
            elif c2[idx] == c1[idx]-1:
                isMatch -=1
            l+=1
        return isMatch == 26
