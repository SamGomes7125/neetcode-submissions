class TimeMap:

    def __init__(self):
        self.h = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.h:
            self.h[key] = [[value,timestamp]]
        else:
            self.h[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.h:
            return ""
        l = 0
        r = len(self.h[key])-1
        answer = ""
        while l <= r:
            mid = (l+r)//2
            if timestamp > self.h[key][mid][1]:
                answer = self.h[key][mid][0]
                l = mid+1
            elif timestamp < self.h[key][mid][1]:
                r = mid-1
            else:
                answer = self.h[key][mid][0]
                break

        return answer

        
