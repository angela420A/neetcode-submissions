class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l <= r:
            m = (l + r) //2

            k = 0
            for p in piles:
                k += math.ceil(float(p) / m)

            if k <= h:
                res = m
                r = m - 1
            else:
                l = m + 1
        return res

        # 1, 2, 3, 4

        # 1/2 = 0.5 => 1
        # 4/2 = 2 => 2
        # 3/2 = 1.5 => 2
        # 2/2 = 1

        # 1 + 2+ 2+1 = 6

        # 1/1 = 1
        # 4/1 = 4
        # 3/1 = 3
        # 2/1 = 2

        # 1 + 4+ 3+ 2 = 10
