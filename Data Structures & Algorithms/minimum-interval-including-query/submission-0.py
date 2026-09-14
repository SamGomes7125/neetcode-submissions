class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        import heapq
        output = [-1] * len(queries)
        heap = []
        intervals.sort(key=lambda x: x[0])
        interval_index = 0
        sorted_queries = sorted(enumerate(queries), key=lambda x: x[1])

        for index, query in sorted_queries:

            shortest = float("inf")

            while interval_index < len(intervals) and intervals[interval_index][0] <= query:

                left, right = intervals[interval_index]
                length = right - left + 1
                heapq.heappush(heap, (length, right))
                interval_index += 1

            while heap and heap[0][1] < query:
                heapq.heappop(heap)

            if heap:
                output[index] = heap[0][0]

        return output

        