class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        in_deg = [0] * (n + 1)
        out_deg = [0] * (n + 1)

        for a, b in trust:
            out_deg[a] += 1
            in_deg[b] += 1

        for i in range(1, n + 1):
            if in_deg[i] == n - 1 and out_deg[i] == 0:
                return i

        return -1