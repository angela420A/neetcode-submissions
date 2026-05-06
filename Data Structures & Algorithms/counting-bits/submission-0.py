class Solution:
    def countBits(self, n: int) -> List[int]:        
        def count_bits(n):
            count = 0
            while n > 0:
                if n & 1:
                    count+=1
                n = n >> 1
            return count
        
        res = [0] * (n+1)
        for i in range(n+1):
            res[i] = count_bits(i)
        return res
        
        