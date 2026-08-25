class CountSquares:

    def __init__(self):
        self.points = {}
        
    def add(self, point: List[int]) -> None:
        point = tuple(point)
        if point not in self.points:
            self.points[point] = 1
        else:    
            self.points[point] += 1
        

    def count(self, point: List[int]) -> int:
        point = tuple(point)
        x1, y1 = point
        count = 0
        for p in self.points:
            x2, y2 = p
            if x1 != x2 and abs(x1 - x2) == abs(y1 - y2):
                corner1 = (x1, y2)
                corner2 = (x2, y1)
                if corner1 in self.points and corner2 in self.points:
                    count += self.points[p] * self.points[corner1] * self.points[corner2]
                else:
                    continue
            else:
                continue
        return count

        
