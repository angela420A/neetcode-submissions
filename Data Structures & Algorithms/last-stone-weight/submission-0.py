class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            y, x = heapq.heappop(stones), heapq.heappop(stones)
            if y == x:
                continue
            
            new_weight = abs(y) - abs(x)
            heapq.heappush(stones, -new_weight)
        return 0 if len(stones) == 0 else abs(stones[0]) 
