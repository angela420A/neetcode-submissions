class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l<=r:
            rate = (l+r)//2

            hours = 0
            for p in piles:
                hours += math.ceil(float(p)/rate)
            
            if hours <= h:
                res = rate
                r = rate - 1
            else:
                l = rate + 1
        return res

        # 1, 2 ,3, 4
        # 0, 1, 2, 3
        # [1] = 2

        # 1/2 = 0.5 = 1
        # 4/2 = 2
        # 3/2 = 1.5 = 2
        # 2/2 = 1
        # 1 + 2 + 2+ 1 = 6