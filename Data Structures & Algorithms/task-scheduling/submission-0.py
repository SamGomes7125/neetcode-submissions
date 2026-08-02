class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        for i in range(len(tasks)):
            if tasks[i] in freq:
                freq[tasks[i]] += 1
            else:
                freq[tasks[i]] = 1
        heap = []
        for value in freq.values():
            heap.append(value)
        for i in range(len(heap)):
            heap[i] = heap[i]*-1
        heapq.heapify(heap)
        from collections import deque

        queue = deque()
        cycle = 0
        while heap or queue:
            cycle+=1

            if len(queue)!=0 and queue[0][1] == cycle:
                cnt, ready_time = queue.popleft()
                heapq.heappush(heap, cnt)

            if heap: 
                cnt = heapq.heappop(heap) + 1
                if cnt < 0:
                    queue.append((cnt, cycle + n + 1))
            
                
        return cycle

        
        



        
        