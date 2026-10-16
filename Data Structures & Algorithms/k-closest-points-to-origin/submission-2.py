class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for x, y in points:
            dist = math.sqrt((x - 0)**2 + (y - 0)**2)
            distances.append((dist, [x, y]))
        
        sort_distances = self.quickSort(distances, 0, len(distances) - 1)

        res = []
        for dist, points in sort_distances:
            res.append(points)
            k -= 1
            if k == 0:
                return res
    
    def quickSort(self, arr, s, e):
        if (e - s + 1) <= 1:
            return arr
        
        pivot = arr[e]
        left = s

        for i in range(s, e):
            if arr[i][0] < pivot[0]:
                temp = arr[i]
                arr[i] = arr[left]
                arr[left] = temp
                left += 1
        
        arr[e] = arr[left]
        arr[left] = pivot

        self.quickSort(arr, s, left - 1)
        self.quickSort(arr, left + 1, e)
        return arr