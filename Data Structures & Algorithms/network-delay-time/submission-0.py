class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, t in times:
            graph[u].append((v, t))

        minHeap = [(0, k)]
        visited = set()
        res = 0

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visited:
                continue
            visited.add(n1)
            res = w1

            for n2, w2 in graph[n1]:
                if n2 not in visited:
                    heapq.heappush(minHeap, (w1 + w2, n2))

        return res if len(visited) == n else -1