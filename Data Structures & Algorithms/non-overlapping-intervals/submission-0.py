class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        prevEnd = intervals[0][1]
        no_of_intervals = 0

        for i in range(1,len(intervals)):           
            if intervals[i][0] < prevEnd:
                no_of_intervals += 1
                prevEnd = min(prevEnd, intervals[i][1])
            else:
                prevEnd = intervals[i][1]
            
        return no_of_intervals
        
        
        