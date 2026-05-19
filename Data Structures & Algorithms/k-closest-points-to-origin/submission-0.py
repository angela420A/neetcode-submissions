class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for x, y in points:
            distance = math.sqrt((x - 0)**2 + (y - 0)**2)
            distances.append([-distance, [x, y]])
        
        heapq.heapify(distances)
        while len(distances) > k:
            heapq.heappop(distances)
        
        res = []
        for distance, point in distances:
            res.append(point)
        return res
        