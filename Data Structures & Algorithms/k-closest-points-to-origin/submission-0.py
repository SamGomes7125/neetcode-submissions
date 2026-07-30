class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        p = []
        for i in range(len(points)):
            p.append(((points[i][0])**2+(points[i][1])**2,i))
        heapq.heapify(p)
        result = []
        while k:
            c = heapq.heappop(p)
            result.append(points[c[1]])
            k-=1
        return result
        